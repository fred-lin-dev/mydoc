---
tags: [meta/guide]
---
# 🎴 Workflow Anki

> **Procédure.** La syntaxe des cartes est fixée par [[Guide-Conventions]] décision 08.
> Ici : la configuration réelle, comment lancer une synchronisation, et les trois
> façons de la casser en silence.

## Prérequis

| | |
|---|---|
| **Anki** installé et **ouvert** | le plugin parle à Anki par HTTP local : Anki fermé = rien ne part |
| Module **AnkiConnect** dans Anki | *Outils → Modules complémentaires → Obtenir des modules* · code **2055492159** · redémarrer Anki |
| Type de note **Basic** avec un champ **Source** | ta configuration écrit le lien vers la note dans ce champ. Si ton Basic n'a que Front/Back, ajoute Source ou vide `FILE_LINK_FIELDS` |
| Plugin **Obsidian_to_Anki** v3.6.0 | récupéré de l'ancien vault, déjà en place et configuré |

## La syntaxe, une seule fois

```markdown
## 🎴 Cartes

Q: Quelles sont les quatre phases de la boucle d'habitude ?
A: Signal → envie → réponse → récompense
<!--ID: 1727384950123-->
```

Deux lignes par carte, `Q:` puis `A:`, **en début de ligne**. La ligne `<!--ID: …-->`
est écrite par le plugin après création.

> ⚠️ **Ne jamais écrire un identifiant à la main.** Le plugin tente alors de mettre à
> jour une carte qui n'existe pas, échoue, et **n'enregistre jamais le fichier**. La
> carte peut rester bloquée des mois sans aucun signal. C'est le piège le plus coûteux
> du dispositif.

## La question doit nommer son sujet

En révision, Anki tire les cartes dans le désordre : **la note n'est pas là**. Un
démonstratif sans référent — « ce principe », « cette règle », « cet effet » —
devient alors impossible à résoudre, et « le livre » ne désigne rien.

Le champ `Source` **ne rattrape pas** ce défaut : il est au dos de la carte.

```markdown
Q: **Engagement et cohérence** — quelle est la défense contre ce levier ?
```

Le préfixe reprend le titre H1 de la note, et **seulement là où la question ne se
suffit pas** : sur une carte de définition, il souffle la réponse. Le test tient
en une lecture de la seule ligne `Q:`. Règle complète : décision 08 des
[[Guide-Conventions]].

**92 cartes sur 350 ont été corrigées ainsi le 2026-09-28** — elles avaient été
rédigées la note sous les yeux, ce qui rend le défaut invisible à l'écriture.

## La configuration appliquée

| Réglage | Valeur | Pourquoi |
|---|---|---|
| Regex `Basic` | `^Q: ((?:.\|\n)*?)\nA: ((?:.\|\n)*?)$` | le motif `(?:.\|\n)` est nécessaire parce qu'en JavaScript `.` ne franchit pas les retours à la ligne |
| `Esprit/` → | `Zettelkasten::Esprit` | un sous-deck par domaine de premier niveau (décision 08b) |
| `Social/` `Tech/` `Langues/` → | `Zettelkasten::Social` `::Tech` `::Langues` | idem |
| Deck par défaut | `Zettelkasten` | filet de sécurité : rien ne tombe dans *Default* |
| Ignorés | `Templates/**` `Scripts/**` `Extras/**` `Meta/**` `Guide-*.md` `Ref-Lecture_*.md` | **`Templates/` est le plus important** : ses `Q:` vides produiraient des cartes vides à chaque scan |
| `ID Comments` | activé | les identifiants en commentaire HTML, invisibles à la lecture |
| `Add File Link` | activé | chaque carte renvoie à sa note d'origine |
| `Add Obsidian Tags` | **désactivé** | un tag `esprit/productivité` deviendrait un tag plat dans Anki, qui utilise `::` pour la hiérarchie |

**Écarté de l'ancien vault :** les 771 entrées de `File Hashes` — elles décrivaient
d'autres fichiers. **Conservés :** les types de note `Cloze` et `Vocabulaire_Elite`
avec leurs regex, inutilisés pour l'instant mais sans conflit possible avec `Q:`/`A:`.

## ⚠️ Ne jamais éditer `data.json` pendant qu'Obsidian tourne

**Le plugin garde ses réglages en mémoire et réécrit son fichier de configuration à chaque
scan.** Une modification faite sur le disque pendant qu'Obsidian est ouvert est donc **écrasée
au scan suivant**, sans aucun message.

*Constaté le 2026-09-28 : l'ajout du domaine `Corps/` au mapping des decks a disparu au premier
scan qui a suivi. Preuve au passage — le fichier était revenu avec ses 174 empreintes de
fichiers, là où je l'avais vidé.*

**Les deux façons correctes de changer un réglage :**

| Méthode | Quand |
|---|---|
| **Le panneau de réglages du plugin**, dans Obsidian | c'est la bonne méthode par défaut. Section *Folder Decks* pour le mapping |
| **Éditer `data.json` avec Obsidian fermé** | pour un changement en masse, ou depuis un script |

> ✅ **L'audit contrôle ce point.** `Scripts/audit.py` vérifie que **tout dossier de domaine
> contenant des `Concept-` figure dans `FOLDER_DECKS`**. Si la configuration a été écrasée, le
> prochain audit le dira — c'est ce qui a permis de le détecter.

## Créer un nouveau domaine : la liste complète

Ajouter un dossier de domaine ne suffit pas. Il faut, dans cet ordre :

1. Créer le dossier — `Corps/` par exemple.
2. Déclarer le domaine dans la table des tags de [[Guide-Conventions]].
3. **Ajouter le mapping dans le panneau de réglages du plugin** : `Corps` → `Zettelkasten::Corps`,
   et le tag de dossier `corps`.
4. Lancer l'audit : s'il ne dit rien, l'étape 3 a bien été enregistrée.

**Si l'étape 3 est oubliée**, les cartes tombent dans le deck par défaut `Zettelkasten` — ce qui
est un filet volontaire, et non `Default`. Rien n'est perdu, mais rien ne le signale non plus
côté Anki.

## La procédure

1. **Ouvrir Anki.** Le laisser ouvert.
2. Dans Obsidian, palette de commandes → **`Obsidian_to_Anki: Scan Vault`**.
3. Lire le rapport affiché : nombre de cartes ajoutées, modifiées, supprimées.
4. Vérifier dans Anki que les cartes sont dans `Zettelkasten::<Domaine>` et **pas**
   dans `Default`.
5. Vérifier qu'une ligne `<!--ID: …-->` est bien apparue sous chaque carte dans les
   notes. **Si aucun identifiant n'apparaît, arrêter** : la synchronisation a échoué
   silencieusement, et relancer ne fera que dupliquer.

## À vérifier au premier scan, une fois pour toutes

- [ ] La regex capture bien deux lignes. Si le plugin ne trouve **aucune** carte, c'est
      elle : remplacer par `^Q: (.*)\nA: (.*)$` dans les réglages du plugin.
- [ ] Aucune carte ne vient de `Templates/` — sinon les globs ignorés ne sont pas pris
      en compte.
- [ ] Aucun fichier `MOC-` n'a produit de carte. C'est interdit par la décision 04, et
      `Scripts/audit.py` le contrôle aussi de son côté.
- [ ] Le champ *Source* des cartes contient bien un lien vers la note.

## Les pièges, par ordre de coût

| Piège | Symptôme | Cause |
|---|---|---|
| **Identifiant écrit à la main** | la carte n'apparaît jamais, le fichier n'est pas enregistré | le plugin met à jour une carte inexistante |
| **Anki fermé** | erreur de connexion, ou silence | rien n'écoute sur le port local |
| **Templates scannés** | cartes vides qui reviennent à chaque scan | globs ignorés mal configurés |
| **Renommage depuis le terminal** | cartes orphelines, liens *Source* morts | voir décision 10 : toujours F2 dans Obsidian |
| **Cartes dans un `MOC-`** | doublons de questions aux réponses divergentes | décision 04 ; indiagnostiquable après mille cartes |
| **Question écrite la note sous les yeux** | la carte est illisible en révision, jamais au moment de l'écrire | le rédacteur a le référent sous les yeux, pas le réviseur |
| **Carte retirée ou déplacée** | une carte reste dans Anki, figée, que plus aucun fichier ne référence | **le plugin crée et met à jour, il ne supprime pas** |

## ⚠️ Le plugin ne supprime jamais rien

**Obsidian_to_Anki crée et met à jour. Il ne supprime pas.** Retirer un bloc `Q:`/`A:`
d'une note, ou **déplacer une idée d'une note vers une autre**, laisse dans Anki une carte
que plus aucun fichier ne référence. Elle ne sera plus jamais mise à jour ni effacée, et
**rien ne le signale** — ni Obsidian, ni le plugin, ni `audit.py`.

L'audit ne peut pas le voir : il est en lecture seule, hors réseau, et Anki n'est pas
toujours ouvert. Le seul contrôle possible compare les deux ensembles d'identifiants :

```bash
python3 Scripts/orphelines.py
```

Il est en lecture seule lui aussi : il **imprime** la commande de suppression, il ne la
lance pas — et il marque `⚠️ DÉJÀ RÉVISÉE` toute carte qui porte un historique, parce que
la supprimer le perdrait. Il détecte les deux sens :

| Symptôme | Cause | Conséquence |
|---|---|---|
| carte dans Anki, absente du vault | un `Q:`/`A:` retiré, ou une idée déplacée | figée pour toujours dans la collection |
| identifiant du vault absent d'Anki | un identifiant écrit à la main, ou une note supprimée dans Anki | **le scan échoue en silence** sur ces cartes |

**À lancer après tout scan qui a retiré ou déplacé une carte.** Constaté le 2026-09-30 en
détachant [[Concept-Signal_Par_L_Absence]] de `Concept-Apparences_Normales` : une carte a
suivi son idée dans la nouvelle note, et l'ancienne est restée dans Anki. **C'est la
comparaison manuelle qui l'a trouvée, pas un contrôle automatique.**

### 🔴 Ne jamais déplacer une carte d'une note à l'autre

**Cette opération n'est pas supportée, et elle échoue de quatre façons différentes.**
Constaté les 2026-09-30 et 10-02 en détachant deux notes. Les quatre pièges se sont
déclenchés l'un après l'autre, chacun masquant le suivant :

| | Ce qui se passe | Comment on s'en aperçoit |
|---|---|---|
| **1** | le plugin **ne supprime pas** la carte retirée du fichier : elle reste dans Anki, figée | `Scripts/orphelines.py` |
| **2** | la carte écrite dans la note cible est **refusée comme doublon** de cette orpheline, sans message | le compte `cartes écrites / synchronisées` |
| **3** | l'empreinte MD5 du fichier est enregistrée **malgré l'échec** : le fichier est sauté aux scans suivants, **la carte n'est jamais retentée** | l'empreinte est égale au md5 du contenu |
| **4** | un **trou** dans la suite des identifiants décale tous les suivants d'un cran, et le scan **écrase** les notes Anki correspondantes avec le mauvais contenu | contrôle d'alignement, ci-dessous |

### 🔴 Le mécanisme du quatrième, et il dépasse largement le déplacement de cartes

**Le plugin apparie les identifiants aux cartes par ordre d'apparition, pas par
adjacence.** Le n-ième identifiant du bloc appartient à la n-ième carte, **où que le
commentaire soit écrit**. Vérifié le 2026-10-02 sur deux notes :

```
fichier : Q1 <ID …321>   Q2 sans id   Q3 <ID …325>
Anki    : …321 = Q1      …325 = le texte de Q2      ← le 2ᵉ id est allé à la 2ᵉ carte
```

**Conséquence, et c'est elle qu'il faut retenir :** une carte sans identifiant placée
**ailleurs qu'en dernier** vole l'identifiant de la suivante. Le scan écrit alors son
contenu dans la note Anki de sa voisine, et la dernière carte perd son identifiant.

> ## ✅ La règle, et elle vaut pour tout ajout de carte
>
> **Une carte sans identifiant doit toujours être la dernière de son bloc.**
>
> Donc : **on ajoute une carte à la fin, jamais au milieu.** Insérer une carte en
> deuxième position dans une note déjà synchronisée suffit à corrompre toutes les
> suivantes — *(déduit du comportement d'appariement confirmé ci-dessus, non testé
> séparément : ne pas l'essayer pour voir)*.
>
> Et si l'ordre logique exige qu'une carte neuve vienne avant les autres : l'écrire en
> dernier, scanner, puis la remonter **avec son identifiant** une fois qu'elle en a un.

> ## ✅ Et la règle pour les trois premiers pièges
>
> **On ne déplace pas une carte. On la supprime d'un côté et on en écrit une neuve de
> l'autre, formulée autrement.**
>
> 1. retirer le `Q:`/`A:` **et son identifiant** de la note d'origine
> 2. scanner → l'orpheline apparaît
> 3. `python3 Scripts/orphelines.py` → la supprimer
> 4. écrire dans la note cible une carte **nouvelle**, dont l'énoncé n'existe nulle part
> 5. scanner
>
> Une formulation neuve ne peut pas être un doublon, donc aucun des quatre pièges ne se
> déclenche. Et c'est de toute façon la bonne pratique : une carte qui change de note
> change de contexte, donc son énoncé doit changer — c'est la règle d'autonomie de la
> décision 08.

### Le contrôle d'alignement, après toute opération sur les cartes

`orphelines.py` compare les **ensembles** d'identifiants, pas leur **placement**. Il ne
voit donc pas le piège 4. Pour le détecter :

```bash
python3 - <<'EOF'
import json, re, pathlib, urllib.request
def anki(a, **p):
    r = urllib.request.urlopen("http://localhost:8765",
        json.dumps({"action": a, "version": 6, "params": p}).encode(), timeout=60)
    return json.load(r)["result"]
paires = []
for d in ("Esprit", "Social", "Tech", "Corps", "Langues"):
    for f in sorted(pathlib.Path(d).glob("Concept-*.md")):
        t = f.read_text(encoding="utf-8")
        if "## 🎴 Cartes" not in t:
            continue
        for m in re.finditer(r"^Q: (.+)\nA: .+$\n<!--ID: (\d+)-->",
                             t.split("## 🎴 Cartes")[1], re.M):
            paires.append((str(f), m.group(1), m.group(2)))
fronts = {str(n["noteId"]): re.sub(r"<[^>]+>", "", n["fields"]["Front"]["value"])
          for n in anki("notesInfo", notes=[int(i) for _, _, i in paires])}
norm = lambda s: re.sub(r"[^a-z0-9]", "", s.lower())[:45]
mal = [(f, q, i) for f, q, i in paires if norm(fronts.get(i, "")) != norm(q)]
print(f"{len(paires)} cartes · {len(mal)} décalée(s)")
for x in mal:
    print("  ", x)
EOF
```

**Réparation d'un décalage :** **tasser les identifiants en tête du bloc** — le n-ième
sur la n-ième carte — et laisser sans identifiant les cartes de la fin. Aucun identifiant
n'est inventé : on les remet là où le plugin les lit déjà. C'est la seule circonstance où
toucher un identifiant à la main est justifié, et elle demande l'accord explicite de
Yinpi.

⚠️ **Première tentative fausse, le 2026-10-02 :** j'avais cru à une insertion « un cran
trop bas » et remonté l'identifiant sur la carte 1 en laissant la 2 sans. Le scan suivant
a donc donné le 2ᵉ identifiant à la carte 2 — c'est-à-dire **écrasé la carte 3 dans
Anki**. Le trou au milieu était la cause, pas le symptôme.

## Combien de cartes sont en jeu aujourd'hui

`grep -c '^Q:'` sur les notes atomiques donne le compte réel, et c'est aussi le
signal de découpe de la décision 01 :

```bash
grep -c '^Q:' Esprit/Concept-*.md Tech/Concept-*.md | awk -F: '{s+=$2} END {print s}'
```

Plus de trois cartes sur des angles différents dans une même note → elle contient
plus d'une idée, elle se scinde.

### 🔗 Connexions
* [[Guide-Conventions]] — *décision 08 : la syntaxe et le découpage des decks.*
* [[Concept-Active_Recall]] · [[Concept-Répétition_Espacée]] — *les deux dispositifs qui justifient tout ce workflow.*
* [[MOC-Audit]] — *les notes sans carte, et le reste des dettes.*
