#!/usr/bin/env python3
"""Audit mécanique du vault — LECTURE SEULE.

Ne modifie jamais rien. Produit un rapport Markdown sur la sortie standard.
La correction est une décision ; le constat, non.

    python3 Scripts/audit.py            # rapport complet
    python3 Scripts/audit.py --erreurs  # erreurs seules

Conventions contrôlées : voir Guide-Conventions.md.
Niveaux de périmètre lus dans Meta/Ref-Périmètre_Bibliothèque.md (décision 12).

⚠️  Ce script a ses propres angles morts. Son compteur n'est pas une vérité :
    le relire de temps en temps sur un échantillon lu à la main.
"""

import datetime
import json
import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
EXCLUS = {".obsidian", ".git", "Templates", "Scripts", "Extras", ".trash"}

BAREME_PERIMETRE = {"fiché", "lu-sans-fiche", "illustration", "dehors"}

# Formats acceptés pour un livre sur le disque. Voir le commentaire du
# recoupement 💾 : l'extension varie, le nom reste mécanique.
FORMATS_LIVRE = {".pdf", ".epub"}

BAREME = {"solide", "contesté", "réfuté", "non évalué", "non applicable", "invérifiable"}

# Ces verdicts exigent une référence **et** une date, et ils se périment.
# `invérifiable` en fait partie : il dit « examiné à cette date, rien ne permettait de
# trancher », et une littérature peut apparaître ensuite. C'est ce qui le distingue de
# `non évalué` (jamais regardé) et de `non applicable` (rien à regarder).
VERDICTS_AVEC_REFERENCE = {"solide", "contesté", "réfuté", "invérifiable"}

# Horizon de péremption. Vieillissent : les trois verdicts tranchés et `🔵
# invérifiable`. Ne vieillissent pas : `⬜`, une définition ne devient pas fausse avec
# le temps, et `⚪`, qui est déjà une dette. Vingt-quatre mois est l'ordre de grandeur auquel une
# méta-analyse ou une réplication large peut renverser une conclusion.
#
# ⚠️  Contrairement à l'ancienne règle des 3 cartes, ce contrôle **se déclenchera
#     tout seul**, par le passage du temps, sans dépendre de la discipline de
#     personne. C'est ce qui distingue un délai d'un quota.
HORIZON_MOIS = 24

# Marqueurs de template oublié. Volontairement peu nombreux : chaque motif ici
# doit être impossible à produire volontairement, sinon il génère du faux positif.
RESTES_TEMPLATE = ["[[]]", "{{title}}", "{{date}}", "[[Concept-]]",
                   "[[Source-]]", "<!-- la question doit nommer"]

LIEN = re.compile(r"\[\[([^\]\[|#^]+)")
CARTE_Q = re.compile(r"^Q:", re.MULTILINE)

# Décision 08, règle d'autonomie : en révision la note n'est pas là, donc une
# question qui désigne son sujet sans le nommer est irrécupérable. Le repérage
# est heuristique — d'où une alerte et non une erreur : seule la lecture tranche.
CARTE_LIGNE = re.compile(r"^Q: (.+)$", re.MULTILINE)
CARTE_AVEC_ID = re.compile(r"^Q: .+\nA: .+$(?:\n<!--ID: (\d+)-->)?", re.MULTILINE)
# Décision 08 : une question qui réclame un item **abstrait** sans nommer ses
# candidats n'a pas de critère de réussite. On ne peut pas savoir si ce qu'on a
# trouvé compte — « quelle nuance escamote-t-il ? » admet dix réponses défendables.
# Repéré par Yinpi en révision sur trois cartes, le 2026-10-02 ; mesuré ensuite sur
# tout le corpus. Heuristique, donc **info** : la réécriture est une décision.
OUVERTE = re.compile(
    # ⚠️ `quelle?` ne couvre PAS « quel » — le `?` porte sur le `e`, donc le motif
    # lisait « quell » ou « quelle ». Bug du 2026-10-02 : toutes les questions en
    # « quel … » passaient à travers, y compris celles qu'on cherchait.
    r"\b(quel(?:le)?s?|qu'est-ce qu[ei])\b[^?]{0,40}\b("
    r"nuances?|inversions?|crit[èe]res?|limites?|faiblesses?|usages?|"
    r"cons[ée]quences?|port[ée]e|failles?|r[ée]serves?|apports?|"
    r"enseignements?|le[çc]ons?)\b",
    re.IGNORECASE,
)
# Ce qui nomme les candidats dans la question, et lève donc le signalement.
CANDIDATS = re.compile(
    r"\bou\b|\bparmi\b|plut[ôo]t que|«|:|\bentre\b|\bdeux\b|\btrois\b"
    r"|\blaquelle\b|\blequel\b", re.IGNORECASE)
CARTES_RELUES = re.compile(r"^cartes_relues: \d{4}-\d{2}-\d{2}", re.MULTILINE)
RELUE = re.compile(r"^atomicite_relue: \d{4}-\d{2}-\d{2}", re.MULTILINE)
LIGNE_MOC = re.compile(r"^\* ([🟢🟠🔴⚪⬜🔵]) \[\[(Concept-[^\]]+)\]\]", re.MULTILINE)
# Une page citée dans une carte doit porter son ouvrage : lue seule, « (p. 61) »
# est l'ordre d'aller vérifier quelque chose qu'on ne peut pas localiser. Forme
# attendue : `(*Titre*, p. N)`. Décidé le 2026-10-03, après relecture des 466 cartes.
PAGE_NUE = re.compile(r"\((?!\*)\s*p\. ?\d")

CARTE_REPONSE = re.compile(r"^A: (.+)$", re.MULTILINE)

# Vocabulaire interne au vault. Une carte parle du monde : lue seule dans Anki,
# « le verdict », « le corpus » ou un symbole du barème ne désignent rien. Contrôlé
# sur les **deux faces** — les trois défauts trouvés le 2026-10-03 étaient répartis
# entre questions et réponses, et le contrôle ne lisait que les questions.
VAULT = re.compile(
    r"\bvault\b|\b(?:ce|du|le) corpus\b|\bles? verdicts?\b"
    r"|\bles auteurs\b(?! de )|[\U0001F7E2\U0001F7E0\U0001F534\u26AA\u2B1C]",
    re.IGNORECASE,
)

IDEE = re.compile(r"^## L'idée[^\n]*\n(.*?)(?=\n## )", re.MULTILINE | re.DOTALL)
CARTE_PREFIXEE = re.compile(r"^\*\*[^*]+\*\* — ")
CITATION = re.compile(r"«[^»]*»")
# Les noms génériques qui désignent « ce dont parle la note ». La liste vient des
# 92 cartes réellement cassées : un démonstratif accolé à l'un d'eux n'a jamais
# de référent dans la carte. Chercher le démonstratif seul produit des faux
# positifs en cascade — « qu'est-ce que », « n'est-ce pas », « ce qu'elle veut ».
GENERIQUES = (
    r"littérature|résultat|score|modèle|principe|concept|procédé|règle|partition"
    r"|livre|idée|loi|distinction|thèse|précepte|critère|analyse|effet|cadre"
    r"|argument|diagnostic|conseil|point|réfutation|exigence|technique|séparation"
    r"|prescription|mécanisme|levier|note|vault"
)
ANAPHORE = re.compile(rf"\b(ce|cet|cette|ces)\s+({GENERIQUES})\b", re.IGNORECASE)
NON_NOMME = re.compile(r"\b((?:l[ea]|du|au|des|aux) livres?|l'auteur|l'ouvrage"
                       r"|cette note|ce vault)\b(?! de )",
                       re.IGNORECASE)
CODE_INLINE = re.compile(r"`[^`]*`")


def sans_emoji(texte):
    """Retire les symboles pour ne comparer que le libellé du barème."""
    return "".join(c for c in texte if unicodedata.category(c) != "So").strip()


def hors_code(contenu):
    """Le contenu privé de son code — blocs ``` et spans `…`.

    Un exemple de convention n'est pas un lien réel : le compter produirait un
    lien mort fantôme, signalé à chaque audit et jamais corrigeable."""
    dedans, garde = False, []
    for ligne in contenu.split("\n"):
        if ligne.lstrip().startswith("```"):
            dedans = not dedans
            continue
        garde.append("" if dedans else CODE_INLINE.sub("", ligne))
    return "\n".join(garde)


def frontmatter(contenu):
    """Parse minimal : (dict, erreur). Pas de dépendance à PyYAML."""
    if not contenu.startswith("---\n"):
        return {}, "frontmatter absent"
    fin = contenu.find("\n---", 3)
    if fin == -1:
        return {}, "frontmatter non fermé"
    champs, cle = {}, None
    for ligne in contenu[4:fin].split("\n"):
        if not ligne.strip():
            continue
        if ligne.startswith((" ", "\t")) and cle:          # continuation
            champs[cle] += " " + ligne.strip()
            continue
        if ":" not in ligne:
            return champs, f"ligne de frontmatter illisible : {ligne.strip()!r}"
        cle, _, valeur = ligne.partition(":")
        cle = cle.strip()
        champs[cle] = valeur.strip()
    return champs, None


def tags_de(champs):
    brut = champs.get("tags", "")
    return [t.strip() for t in brut.strip("[]").split(",") if t.strip()]


def longueur_idee(contenu):
    """Le nombre de mots de prose de la section « L'idée ».

    Pourquoi cette section et pas la note entière : une longue section de
    vérification est un bon signe, une longue idée en est un mauvais. Les lignes
    de tableau, de citation et de code sont retirées — sinon on mesure la mise en
    forme. Le titre tolère un complément (« L'idée — telle qu'elle circule »), qui
    est une bonne pratique et non un écart.
    """
    m = IDEE.search(contenu)
    if not m:
        return None
    prose = [l for l in m.group(1).split("\n")
             if not l.lstrip().startswith(("|", ">", "```"))]
    return len(" ".join(prose).split())


def notes():
    for chemin in sorted(RACINE.rglob("*.md")):
        if set(chemin.relative_to(RACINE).parts) & EXCLUS:
            continue
        yield chemin


def perimetre():
    """(niveaux, possedes, nom_du_fichier) depuis l'inventaire de la bibliothèque.

    Colonnes attendues : Fichier | 💾 | Niveau | Domaine | Liste.
    """
    ref = RACINE / "Meta" / "Ref-Bibliothèque.md"
    if not ref.exists():
        return {}, {}, "Meta/Ref-Bibliothèque.md"
    niveaux, possedes = {}, {}
    for ligne in ref.read_text(encoding="utf-8").split("\n"):
        cellules = [c.strip() for c in ligne.split("|")[1:-1]]
        if len(cellules) >= 3 and cellules[2] in BAREME_PERIMETRE:
            niveaux[cellules[0]] = cellules[2]
            possedes[cellules[0]] = cellules[1] == "✅"
    return niveaux, possedes, f"Meta/{ref.name}"


def main():
    erreurs, alertes, infos = [], [], []
    fichiers = list(notes())
    if not fichiers:
        print("Aucune note à auditer.")
        return 0

    contenus = {f: f.read_text(encoding="utf-8") for f in fichiers}
    noms = defaultdict(list)
    for f in fichiers:
        noms[f.stem].append(f.relative_to(RACINE))

    cibles = set(noms) | {p.name for p in RACINE.rglob("*") if p.is_file()}
    entrants = defaultdict(set)
    niveaux, possedes, NOM_REF = perimetre()
    ages = {}

    for f, contenu in contenus.items():
        rel, nom = f.relative_to(RACINE), f.stem
        champs, err = frontmatter(contenu)
        prefixe = nom.split("-")[0] if "-" in nom else ""

        if err:
            erreurs.append((rel, err))

        for tag in tags_de(champs):
            if tag.endswith("/"):
                erreurs.append((rel, f"tag placeholder non complété : `{tag}`"))

        for cible in LIEN.findall(hors_code(contenu)):
            cible = cible.strip()
            if not cible:
                continue
            entrants[cible].add(nom)
            if cible not in cibles and f"{cible}.md" not in cibles:
                erreurs.append((rel, f"lien mort : `[[{cible}]]`"))

        for reste in RESTES_TEMPLATE:
            if reste in contenu:
                alertes.append((rel, f"reste de template : `{reste}`"))

        nb_cartes = len(CARTE_Q.findall(contenu))

        # Le plugin apparie les identifiants aux cartes **par ordre d'apparition**,
        # pas par adjacence : le n-ième identifiant va à la n-ième carte. Une carte
        # sans identifiant placée ailleurs qu'en dernier vole donc celui de sa
        # voisine, et le prochain scan écrase une note Anki avec le mauvais contenu.
        # Ça s'est produit le 2026-10-02. Hors réseau, donc contrôlable ici.
        if "## 🎴 Cartes" in contenu:
            suite = [bool(m.group(1)) for m in
                     CARTE_AVEC_ID.finditer(contenu.split("## 🎴 Cartes")[1])]
            if any(not suite[i] and any(suite[i + 1:]) for i in range(len(suite))):
                erreurs.append(
                    (rel, "carte sans identifiant suivie d'une carte qui en a un — "
                          "le prochain scan écrasera la mauvaise note Anki. "
                          "Une carte neuve va **en dernier** (décision 08)")
                )

        if not CARTES_RELUES.search(contenu):
            for question in CARTE_LIGNE.findall(contenu):
                if OUVERTE.search(question) and not CANDIDATS.search(question):
                    infos.append(
                        (rel, f"question ouverte, sans critère de réussite : "
                              f"`{question[:62]}…` — nommer les candidats, ou "
                              "`cartes_relues:` si elle est acceptable (décision 08)")
                    )

        for question in CARTE_LIGNE.findall(contenu):
            nu = CITATION.sub("", question)
            motif = (NON_NOMME.search(nu) if CARTE_PREFIXEE.match(nu)
                     else ANAPHORE.search(nu) or NON_NOMME.search(nu))
            if motif:
                alertes.append(
                    (rel, f"carte sans contexte — « {motif.group(0)} » sans référent : "
                          f"`{question[:60]}…` (règle d'autonomie, décision 08)")
                )

        for face, ligne in ([("question", q) for q in CARTE_LIGNE.findall(contenu)]
                            + [("réponse", a) for a in CARTE_REPONSE.findall(contenu)]):
            m = VAULT.search(CITATION.sub("", ligne))
            if m:
                alertes.append(
                    (rel, f"carte qui parle du vault — « {m.group(0)} » dans la {face} : "
                          f"`{ligne[:55]}…` (une carte parle du monde, décision 08)")
                )
            if PAGE_NUE.search(ligne):
                alertes.append(
                    (rel, f"page sans ouvrage dans la {face} : `{ligne[:55]}…` — "
                          "forme attendue `(*Titre*, p. N)` (décision 08)")
                )

        if prefixe == "Concept":
            verdict = sans_emoji(champs.get("fiabilite", ""))
            if "fiabilite" not in champs:
                erreurs.append((rel, "champ `fiabilite` absent — il est obligatoire"))
            elif verdict not in BAREME:
                erreurs.append((rel, f"verdict hors barème : `{verdict}`"))
            elif verdict in VERDICTS_AVEC_REFERENCE:
                if not champs.get("fiabilite_note", "").strip(' "'):
                    erreurs.append(
                        (rel, f"`{verdict}` sans `fiabilite_note` — un verdict "
                              "sans référence est un avis")
                    )
                brut = champs.get("fiabilite_date", "").strip(' "')
                if not brut:
                    erreurs.append(
                        (rel, f"`{verdict}` sans `fiabilite_date` — un verdict "
                              "sans date ne peut pas se périmer")
                    )
                else:
                    try:
                        etabli = datetime.date.fromisoformat(brut)
                    except ValueError:
                        erreurs.append((rel, f"`fiabilite_date: {brut}` illisible "
                                             "— format attendu AAAA-MM-JJ"))
                    else:
                        ages[rel] = (datetime.date.today() - etabli).days
                        if ages[rel] > HORIZON_MOIS * 30:
                            infos.append(
                                (rel, f"dette : verdict `{verdict}` établi le {brut}, "
                                      f"soit il y a {ages[rel] // 30} mois — à revérifier")
                            )
            if verdict == "non évalué":
                infos.append((rel, "dette : non évalué"))
            if not champs.get("source", "").strip(' "'):
                infos.append((rel, "sans `source`"))
            if nb_cartes == 0:
                alertes.append((rel, "aucune carte de révision (dette, décision 08)"))
            elif nb_cartes > 3:
                infos.append(
                    (rel, f"{nb_cartes} cartes — candidate à la scission (règle des 3)")
                )

        if prefixe == "MOC" and nb_cartes:
            erreurs.append(
                (rel, f"{nb_cartes} carte(s) dans un index — interdit (décision 04)")
            )

    # Garde-fou 11 : une fiche de livre fiché doit produire au moins une note.
    fiches, converties = 0, 0
    for f in fichiers:
        if not f.stem.startswith("Source-"):
            continue
        fiches += 1
        titre = f.stem[len("Source-"):]
        citee_par = entrants.get(f.stem, set())
        concepts = {n for n in citee_par if n.startswith("Concept-")}
        if concepts:
            converties += 1
        elif niveaux.get(titre) == "fiché":
            erreurs.append(
                (f.relative_to(RACINE),
                 "aucune note atomique : un livre fiché doit produire au moins "
                 "un `Concept-` (garde-fou 11)")
            )
        if niveaux.get(titre) in {"lu-sans-fiche", "dehors"}:
            alertes.append(
                (f.relative_to(RACINE),
                 f"fiche créée alors que le livre est classé "
                 f"`{niveaux[titre]}` — contredit le périmètre")
            )

    for doublon, chemins in sorted(noms.items()):
        if len(chemins) > 1:
            erreurs.append((chemins[0], f"doublon de nom : {', '.join(map(str, chemins))}"))

    # Tout dossier de domaine doit être connu du plugin Anki, sinon ses cartes
    # tombent dans le deck par défaut sans que rien ne le signale.
    conf = RACINE / ".obsidian/plugins/obsidian-to-anki-plugin/data.json"
    if conf.exists():
        try:
            decks = json.loads(conf.read_text(encoding="utf-8"))["settings"]["FOLDER_DECKS"]
        except (ValueError, KeyError):
            erreurs.append((Path(conf.name), "configuration du plugin Anki illisible"))
        else:
            domaines = {d.name for d in RACINE.iterdir()
                        if d.is_dir() and not d.name.startswith(".")
                        and d.name not in EXCLUS and any(d.glob("Concept-*.md"))}
            for d in sorted(domaines - {k for k, v in decks.items() if v}):
                erreurs.append(
                    (Path(".obsidian/plugins/obsidian-to-anki-plugin/data.json"),
                     f"domaine `{d}/` absent de FOLDER_DECKS — ses cartes iront "
                     f"dans le deck par défaut")
                )

    # Échantillon de relecture pour l'atomicité (décision 01). Ce n'est **pas** un
    # verdict : aucun compteur ne sait dire si une note porte deux idées. Le seuil
    # est le 9ᵉ décile de la distribution courante, donc le contrôle renvoie
    # toujours environ un dixième des notes — c'est son objet. Il choisit
    # l'échantillon que la décision 09 demande de relire à la main, au lieu de le
    # tirer au hasard.
    longueurs = {}
    for f in fichiers:
        if f.stem.startswith("Concept-"):
            n = longueur_idee(f.read_text(encoding="utf-8"))
            if n:
                longueurs[f] = n
    if len(longueurs) >= 20:
        seuil = sorted(longueurs.values())[int(0.90 * (len(longueurs) - 1))]
        for f, n in sorted(longueurs.items(), key=lambda x: -x[1]):
            if n <= seuil:
                continue
            # Le seuil est relatif, donc il renvoie toujours un dixième des notes :
            # sans mémoire de ce qui a été relu, la file ne pourrait jamais se vider
            # et le travail de relecture ne laisserait aucune trace. Le champ
            # `atomicite_relue` la rend finie — même motif que `fiabilite_date`.
            if RELUE.search(f.read_text(encoding="utf-8")):
                continue
            infos.append((f.relative_to(RACINE),
                          f"à relire pour l'atomicité : {n} mots d'idée, "
                          f"dernier décile (seuil {seuil})"))

    # Un MOC est un index (décision 04) : un index qui omet des entrées ne fait pas
    # son travail, et un index qui annonce un faux verdict désinforme. Trois dérives
    # de ce genre ont été trouvées à la main avant que ce contrôle existe — dont une
    # section entière de quatre notes absente de MOC-Social.
    for domaine in sorted(d.name for d in RACINE.iterdir()
                          if d.is_dir() and not d.name.startswith(".")
                          and d.name not in EXCLUS and d.name != "Meta"):
        moc = RACINE / domaine / f"MOC-{domaine}.md"
        if not moc.exists():
            continue
        listees = {m.group(2): m.group(1) for m in
                   LIGNE_MOC.finditer(moc.read_text(encoding="utf-8"))}
        for f in sorted((RACINE / domaine).glob("Concept-*.md")):
            verdict = frontmatter(f.read_text(encoding="utf-8"))[0].get("fiabilite", "")[:1]
            if f.stem not in listees:
                alertes.append((moc.relative_to(RACINE),
                                f"`{f.stem}` n'est listée nulle part dans cet index"))
            elif verdict and listees[f.stem] != verdict:
                erreurs.append((moc.relative_to(RACINE),
                                f"`{f.stem}` : l'index annonce {listees[f.stem]}, "
                                f"la note porte {verdict}"))

        # Les compteurs de l'en-tête sont des données dérivées, et ils ont dérivé deux
        # fois avant ce contrôle.
        reels = defaultdict(int)
        for f in (RACINE / domaine).glob("Concept-*.md"):
            reels[frontmatter(f.read_text(encoding="utf-8"))[0].get("fiabilite", "")[:1]] += 1
        texte_moc = moc.read_text(encoding="utf-8")
        total = re.search(r"\*\*(\d+) notes atomiques", texte_moc)
        if total and int(total.group(1)) != sum(reels.values()):
            alertes.append((moc.relative_to(RACINE),
                            f"l'en-tête annonce {total.group(1)} notes, il y en a "
                            f"{sum(reels.values())}"))
        for emoji, libelle in (("🟢", "solide"), ("🟠", "contesté"), ("🔴", "réfuté"),
                               ("⬜", "non applicable"), ("⚪", "non évalué"),
                               ("🔵", "invérifiable")):
            m = re.search(rf"^\| {emoji} {libelle} \| \**(\d+)\**", texte_moc, re.M)
            if m and int(m.group(1)) != reels[emoji]:
                alertes.append((moc.relative_to(RACINE),
                                f"le tableau annonce {m.group(1)} notes {emoji}, "
                                f"il y en a {reels[emoji]}"))

    # Le tableau de bord Dataview doit interroger tous les domaines. Il a été
    # aveugle à `Corps/` depuis la naissance de ce domaine, sans que rien le dise :
    # même angle mort que FOLDER_DECKS côté Anki, et même correctif.
    tableau = RACINE / "Meta" / "MOC-Audit.md"
    if tableau.exists():
        contenu_tb = tableau.read_text(encoding="utf-8")
        domaines_reels = {d.name for d in RACINE.iterdir()
                          if d.is_dir() and not d.name.startswith(".")
                          and d.name not in EXCLUS and d.name != "Meta"}
        for i, ligne in enumerate(contenu_tb.split("\n"), 1):
            if not ligne.startswith("FROM "):
                continue
            cites = set(re.findall(r'"([^"]+)"', ligne))
            for absent in sorted(domaines_reels - cites):
                erreurs.append((Path("Meta/MOC-Audit.md"),
                                f"ligne {i} : le domaine `{absent}/` est absent du "
                                f"`FROM` — ses notes sont invisibles au tableau de bord"))

    # Le format n'est pas la règle : la décision 02 exige que `Source-<titre>`
    # ↔ `<titre>.<ext>` reste une transformation mécanique, pas que l'extension
    # soit `.pdf`. Un EPUB était invisible ici, donc une ligne 💾 ✅ légitime
    # produisait « marqué ✅ mais absent ». Constaté le 2026-10-02 avec Exercised.
    pdfs = {p.stem for p in RACINE.rglob("*")
            if p.suffix.lower() in FORMATS_LIVRE}
    for absent in sorted(pdfs - set(niveaux)):
        alertes.append((Path(NOM_REF),
                        f"livre hors inventaire : `{absent}` n'a aucun niveau"))

    # La colonne 💾 se recoupe avec le disque, sinon elle dérive en silence.
    for titre, dit_possede in sorted(possedes.items()):
        if dit_possede and titre not in pdfs:
            erreurs.append((Path(NOM_REF),
                            f"`{titre}` est marqué ✅ mais absent d'`Extras/Books/`"))
        elif not dit_possede and titre in pdfs:
            erreurs.append((Path(NOM_REF),
                            f"`{titre}` est sur le disque mais marqué non possédé"))

    # Le garde-fou 11 ne voyait qu'une fiche sans note. Un livre fiché sans
    # fiche du tout restait invisible : huit dormaient ainsi.
    for titre, niveau in sorted(niveaux.items()):
        if niveau == "fiché" and titre not in {f.stem[len("Source-"):] for f in fichiers
                                               if f.stem.startswith("Source-")}:
            infos.append((Path(NOM_REF), f"dette : `{titre}` est fiché, sans fiche `Source-`"))

    for f in fichiers:
        if f.stem.split("-")[0] in {"Concept", "Source"} and not entrants.get(f.stem):
            infos.append((f.relative_to(RACINE), "orpheline : aucun lien entrant"))

    # ------------------------------------------------------------------ rapport
    erreurs_seules = "--erreurs" in sys.argv
    print("# Rapport d'audit\n")
    print(f"- notes auditées : **{len(fichiers)}**")
    print(f"- livres dans `Extras/` : **{len(pdfs)}**")
    print(f"- fiches `Source-` : **{fiches}**")
    print(f"- fiches ayant produit au moins une note : **{converties}**")
    if ages:
        vieux = max(ages.values())
        bientot = sum(1 for j in ages.values() if HORIZON_MOIS * 30 - 180 < j <= HORIZON_MOIS * 30)
        print(f"- verdicts tranchés : **{len(ages)}**, le plus ancien a "
              f"**{vieux // 30} mois** · horizon {HORIZON_MOIS} mois"
              + (f" · **{bientot}** à moins de 6 mois de l'échéance" if bientot else ""))
    print(f"\n→ **{len(erreurs)} erreurs · {len(alertes)} alertes · {len(infos)} infos**\n")

    sections = [("🔴 Erreurs", erreurs)]
    if not erreurs_seules:
        sections += [("🟠 Alertes", alertes), ("⚪ Dette et informations", infos)]

    for titre, items in sections:
        print(f"\n## {titre} — {len(items)}\n")
        if not items:
            print("*rien.*")
            continue
        par_fichier = defaultdict(list)
        for chemin, message in items:
            par_fichier[str(chemin)].append(message)
        for chemin in sorted(par_fichier):
            print(f"\n**{chemin}**")
            for message in par_fichier[chemin]:
                print(f"- {message}")

    return 1 if erreurs else 0


if __name__ == "__main__":
    sys.exit(main())
