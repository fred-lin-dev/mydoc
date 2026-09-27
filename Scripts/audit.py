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

import json
import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
EXCLUS = {".obsidian", ".git", "Templates", "Scripts", "Extras", ".trash"}

BAREME = {"solide", "contesté", "réfuté", "non évalué", "non applicable"}
VERDICTS_AVEC_REFERENCE = {"solide", "contesté", "réfuté"}

# Marqueurs de template oublié. Volontairement peu nombreux : chaque motif ici
# doit être impossible à produire volontairement, sinon il génère du faux positif.
RESTES_TEMPLATE = ["[[]]", "{{title}}", "{{date}}", "[[Concept-]]", "[[Source-]]"]

LIEN = re.compile(r"\[\[([^\]\[|#^]+)")
CARTE_Q = re.compile(r"^Q:", re.MULTILINE)
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


def notes():
    for chemin in sorted(RACINE.rglob("*.md")):
        if set(chemin.relative_to(RACINE).parts) & EXCLUS:
            continue
        yield chemin


def perimetre():
    """{stem_du_pdf: niveau} depuis la note de référence."""
    ref = RACINE / "Meta" / "Ref-Périmètre_Bibliothèque.md"
    niveaux = {}
    if not ref.exists():
        return niveaux
    for ligne in ref.read_text(encoding="utf-8").split("\n"):
        cellules = [c.strip() for c in ligne.split("|")[1:-1]]
        if len(cellules) >= 2 and cellules[1] in {"fiché", "lu-sans-fiche", "illustration", "dehors"}:
            niveaux[cellules[0]] = cellules[1]
    return niveaux


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
    niveaux = perimetre()

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

    pdfs = {p.stem for p in RACINE.rglob("*.pdf")}
    for absent in sorted(pdfs - set(niveaux)):
        alertes.append((Path("Meta/Ref-Périmètre_Bibliothèque.md"),
                        f"PDF hors périmètre : `{absent}` n'a aucun niveau"))

    for f in fichiers:
        if f.stem.split("-")[0] in {"Concept", "Source"} and not entrants.get(f.stem):
            infos.append((f.relative_to(RACINE), "orpheline : aucun lien entrant"))

    # ------------------------------------------------------------------ rapport
    erreurs_seules = "--erreurs" in sys.argv
    print("# Rapport d'audit\n")
    print(f"- notes auditées : **{len(fichiers)}**")
    print(f"- PDF dans `Extras/` : **{len(pdfs)}**")
    print(f"- fiches `Source-` : **{fiches}**")
    print(f"- fiches ayant produit au moins une note : **{converties}**")
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
