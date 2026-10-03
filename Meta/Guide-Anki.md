---
tags: [meta/guide]
---
# 🎴 Anki — rédiger, puis synchroniser

> **Procédure, dans l'ordre réel du travail :** on écrit une carte, puis on la
> synchronise. Les règles opposables sont la **décision 08** de
> [[Guide-Conventions]] ; ici la pratique et la mécanique.
>
> La partie **Rédiger** vient de la relecture des **466 cartes une par une dans
> Anki**, le 2026-10-03. La partie **Synchroniser** vient des pannes réelles.

---

# Partie 1 · Rédiger

## Le principe central : une carte porte une limite, pas une définition

C'est le constat de la relecture complète, et il n'était pas prévu. Ce qui distingue
ce paquet d'un paquet de définitions, c'est que **sur les trois cartes d'une note, il
y en a typiquement une qui dit ce que l'idée ne permet pas.**

| Note | La carte qui porte la limite |
|---|---|
| Effet Lindy | *« La survie n'est pas la vérité. L'astrologie est très Lindy, la saignée a duré deux mille ans. Il prédit la durée, pas la validité. »* |
| Antifragilité | *« Il se diagnostique après coup : ce qui survit est déclaré antifragile. L'étiquetage est rétrospectif, donc sans valeur prédictive. »* |
| Boucle de rétroaction | *« Nommer une boucle donne l'impression d'expliquer. Sans le gain ni les délais, rien n'est prédit. »* |
| Rationalité limitée | *« Il peut excuser n'importe quoi. Certains acteurs choisissent de ne pas s'informer — c'est une décision, pas une contrainte. »* |
| Dichotomie du contrôle | *« Les cas intermédiaires sont la majorité. Elle vaut comme gradient, pas comme partition nette. »* |

**Pourquoi ça compte pour la révision à long terme : une définition se périme, une
limite se vérifie.** Dans cinq ans, « qu'est-ce que l'ego depletion » sera une
question d'archive ; « pourquoi la méthode tient quand même » restera une question
vivante. La limite est aussi ce qui empêche la carte de devenir un slogan.

> **Le test, avant d'écrire la troisième carte :** *qu'est-ce que cette idée ne me
> permet pas de conclure ?* Si la réponse ne vient pas, la note n'est peut-être pas
> vérifiée — voir le champ `fiabilite`, décision 05.

---

## La forme du trio

Trois cartes, et chacune fait un travail différent. C'est une régularité constatée,
pas une obligation.

| | Ce qu'elle demande | Exemple réel |
|---|---|---|
| **1** | l'idée, ou sa définition exacte | *« Qu'est-ce qu'un centre de gravité, et qu'est-ce que ce n'est pas ? »* |
| **2** | le mécanisme, ou la distinction qui la rend utilisable | *« Quelle est la différence entre friction et brouillard ? »* |
| **3** | **la limite**, le contresens, ou la partie contestée | *« Quelle est la limite décisive de l'effet Lindy ? »* |

**Deux cartes suffisent souvent.** 19 notes du vault en ont deux et s'en portent
bien. Écrire la troisième parce que la règle dit trois est le piège décrit plus bas.

---

## Les cinq tests d'autonomie

La carte sera lue **sans la note, sans la carte précédente, des mois plus tard**.
Chaque test ci-dessous a attrapé de vraies fautes dans ce vault.

| Test | Refusé | Corrigé en |
|---|---|---|
| **1 · Le sujet est nommé** | `quelle est la défense contre ce levier ?` | `**Engagement et cohérence** — quelle est la défense contre ce levier ?` |
| **2 · L'ouvrage est nommé** | `quelles trois affirmations le livre présente-t-il ?` | `van der Kolk réunit trois affirmations : lesquelles…` |
| **3 · La carte parle du monde** | `pourquoi cette thèse reçoit-elle ⬜ non applicable ?` | `pourquoi cette thèse n'est-elle ni vraie ni fausse ?` |
| **4 · La page porte son ouvrage** | `…paraissent familières (p. 61)` | `…paraissent familières (*Style*, p. 61)` |
| **5 · La réponse se tient seule** | une réponse qui renvoie à une autre note du vault | l'information est recopiée, ou la carte est supprimée |

**Le test 3 est le moins intuitif et le plus violé.** Le barème `fiabilite`, « le
corpus », « le vault », « les auteurs » sont des conventions d'ici : **demander
pourquoi une note est classée `⬜` n'est pas une question sur le monde.** Cinq cartes
le faisaient.

**Les tests 2 et 5 portent aussi sur la réponse.** Deux des trois défauts trouvés le
2026-10-03 étaient dans des réponses, alors que le contrôle ne lisait que les
questions. Il lit maintenant les deux faces.

---

## Quand ne PAS mettre de préfixe

**Le préfixe `**Titre** — ` se met si et seulement si la question ne se suffit pas.**
Sur une carte de définition, il souffle la réponse :

```
✗  **Active recall** — qu'est-ce qui consolide une information :
   la réexposition ou la récupération ?
        ↑ le préfixe donne la réponse

✓  Qu'est-ce qui consolide une information : la réexposition
   ou la récupération ?
```

Sur 466 cartes, **124 portent un préfixe et 342 n'en ont pas besoin.** Le préfixe est
une réparation, pas un ornement.

---

## Les pièges de rédaction

| Piège | Pourquoi il est invisible à l'écriture |
|---|---|
| **Écrire la note sous les yeux** | le référent de « ce principe » est devant toi et pas devant le réviseur. **92 cartes sur 350 ont dû être reprises pour ça.** C'est le seul défaut qu'aucune relecture de la note ne révèle |
| **Le quota de trois** | écrire trois cartes parce que la règle en annonce trois. La règle disait « plus de trois → scinder » : elle mesurait sa propre observance et n'a jamais pu se déclencher. Voir décision 01 |
| **La réponse-étiquette** | une réponse d'un seul terme ne se révise pas : elle se reconnaît. Une bonne réponse tient en une à trois phrases et contient le *pourquoi* |
| **La réponse dans la question** | `pourquoi la posture de pouvoir est-elle réfutée ?` annonce le verdict. Préférer `quel est le statut de la posture de pouvoir ?` |
| **La page nue** | `(p. 61)` est l'ordre d'aller vérifier ce qu'on ne peut pas localiser — le pire état pour une méthode fondée sur la citation vérifiable |

---

## Les contrôles mécaniques, et ce qu'ils ne savent pas faire

`python3 Scripts/audit.py` refuse automatiquement :

* un démonstratif accolé à un nom générique dans une question sans préfixe ;
* `le livre`, `du livre`, `l'auteur`, `les auteurs` non suivis de « de » ;
* le vocabulaire interne du vault, **sur les deux faces** ;
* une parenthèse de page qui ne commence pas par un titre en italique.

Les repères canoniques d'une autre nature — `(B 19)` pour Kant, `(A 421 / B 449)` —
sont épargnés : ils identifient l'édition par eux-mêmes.

> ⚠️ **Aucun de ces contrôles ne lit une carte.** Ils attrapent des motifs. Ils ne
> savent pas si une réponse est juste, si une question a une seule réponse, ni si la
> carte apprend quelque chose. **Le seul test qui compte reste la lecture à voix
> haute de la carte, seule, sans rien sous les yeux** — et c'est ainsi que les 23
> fautes du 2026-10-03 ont été trouvées, pas par le script.

---

---

# Partie 2 · Synchroniser

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

### La seconde syntaxe — `Vocabulaire_Elite`, pour les fiches `Vocab-`

**Une ligne par mot, et elle produit deux cartes.** Mise en service le 2026-10-03, après
avoir dormi configurée depuis le premier jour.

```markdown
**sophisme** :: raisonnement faux présenté comme valide, et présenté ainsi à dessein. *Ex : « tout le monde le fait » n'est pas un argument mais un sophisme.*
```

| Partie | Va dans le champ | Obligatoire |
|---|---|---|
| `**mot**` | `Front` | oui — **les astérisques font partie de la capture**, le champ reçoit `<strong>mot</strong>` |
| ` :: ` | — | oui, **espace de chaque côté** |
| la définition | `Back` | oui |
| ` *Ex : …*` | `Exemple` | non |
| le lien vers la note | `Source` | ajouté par le plugin |

**Les deux cartes générées, et c'est tout l'intérêt du type :**

| Carte | Sens | À quoi elle sert |
|---|---|---|
| 1 | mot → définition | reconnaître un mot lu ou entendu |
| 2 | **définition → mot** | **produire le mot en parlant** — le seul sens qui rend plus articulé, et impossible avec `Basic` |

> ⚠️ **Trois contraintes de rédaction, toutes dues à la regex.**
> 1. **Une seule ligne.** La regex est ancrée sur `$` sans `(?:.|\n)`, contrairement à
>    celle de `Basic` : une définition sur deux lignes n'est pas vue du tout.
> 2. **Pas de ` :: ` dans la définition**, qui couperait au mauvais endroit.
> 3. **L'exemple se termine par `*` en fin de ligne.** Un astérisque de fermeture oublié
>    fait avaler l'exemple par le champ `Back`, sans erreur visible.
>
> ✅ **Testable sans Anki**, et ça a été fait avant le premier scan :
> ```bash
> python3 -c "
> import re,io,sys
> rx=re.compile(r'^(\*\*.*?\*\*) :: (.*?)(?: \*Ex\s?: (.*?)\*)?\$', re.M)
> t=io.open(sys.argv[1],encoding='utf-8').read()
> for m in rx.finditer(t): print(m.group(1), '| Ex:', bool(m.group(3)))
> " Lexique/Vocab-Nommer_Un_Raisonnement.md
> ```

## La configuration appliquée

| Réglage | Valeur | Pourquoi |
|---|---|---|
| Regex `Basic` | `^Q: ((?:.\|\n)*?)\nA: ((?:.\|\n)*?)$` | le motif `(?:.\|\n)` est nécessaire parce qu'en JavaScript `.` ne franchit pas les retours à la ligne |
| `Esprit/` → | `Zettelkasten::Esprit` | un sous-deck par domaine de premier niveau (décision 08b) |
| `Social/` `Tech/` `Lexique/` → | `Zettelkasten::Social` `::Tech` `::Lexique` | idem |
| `Drills/Anglais/` → | **`Anglais`** | hors de `Zettelkasten::` : du drill, pas du savoir. Il a besoin de sa propre entrée — le plugin résout le deck sur le chemin **exact**, il ne remonte pas au parent |
| Regex `Vocabulaire_Elite` | `^(\*\*.*?\*\*) :: (.*?)(?: \*Ex\s?: (.*?)\*)?$` | une ligne par mot, deux cartes par ligne — voir plus haut |
| Deck par défaut | `Zettelkasten` | filet de sécurité : rien ne tombe dans *Default* |
| Ignorés | `Templates/**` `Scripts/**` `Extras/**` `Meta/**` `Guide-*.md` `Ref-Lecture_*.md` | **`Templates/` est le plus important** : ses `Q:` vides produiraient des cartes vides à chaque scan |
| `ID Comments` | activé | les identifiants en commentaire HTML, invisibles à la lecture |
| `Add File Link` | activé | chaque carte renvoie à sa note d'origine |
| `Add Obsidian Tags` | **désactivé** | un tag `esprit/productivité` deviendrait un tag plat dans Anki, qui utilise `::` pour la hiérarchie |

**Écarté de l'ancien vault :** les 771 entrées de `File Hashes` — elles décrivaient
d'autres fichiers. **Conservés :** les types de note `Cloze` et `Vocabulaire_Elite`
avec leurs regex, sans conflit possible avec `Q:`/`A:`.

> **Et `Vocabulaire_Elite` a servi, un an après avoir été conservé « au cas où ».**
> Le type existait dans Anki avec ses deux gabarits, sa regex était dans la config, le
> deck `Langues` était mappé — **et zéro note l'avait employé.** Mis en service le
> 2026-10-03 par l'ouverture de `Langues/Français/`. C'est le seul élément repris de
> l'ancien vault qui se soit révélé utile sans être retouché, et il vaut d'être noté
> comme tel : **garder un réglage inutilisé a eu un rendement, une fois.**

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
4. Créer son index `MOC-<Domaine>` — l'audit compare les notes à son contenu, et une
   note non listée devient une alerte.
5. Lancer l'audit : s'il ne dit rien, l'étape 3 a bien été enregistrée.

> ⚠️ **Un sous-dossier compte comme un dossier à part entière** — ajouté le 2026-10-03.
> `Drills/Anglais` a sa propre entrée dans `FOLDER_DECKS`, et **l'audit vérifie
> désormais tout dossier porteur de cartes, pas seulement ceux de premier niveau.**
> Avant ce correctif, perdre le mapping d'un sous-dossier n'aurait rien déclenché :
> exactement l'angle mort qui avait coûté le mapping de `Corps/` le 2026-09-28, mais un
> cran plus bas et donc invisible au contrôle d'alors.
>
> *Le contrôle a été écrit pour `Langues/Français/`, qui a disparu le jour même ; il
> garde tout son objet pour `Drills/Anglais` — et c'est `Drills/` qui est désormais le
> seul dossier à deux niveaux porteur de cartes.*

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
for d in ("Esprit", "Social", "Tech", "Corps", "Lexique"):
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

### ⚠️ Un scan peut ne rien prendre, et les contrôles disaient « ✅ » — 2026-10-03

**Le symptôme.** Deux fichiers neufs, un scan lancé, `audit.py` à 0 · 0 · 0 et
`orphelines.py` affichant *« les deux ensembles coïncident exactement »*. Tout avait
l'air réussi. **Le scan n'avait rien pris du tout.**

| Ce qui a trompé | Pourquoi ce n'était pas un mensonge |
|---|---|
| `audit.py` 0 · 0 · 0 | il ne contrôle **pas** la synchronisation : il est hors réseau, c'est écrit dans son en-tête |
| `orphelines.py` ✅ | il compare des **identifiants**. Une carte écrite qui n'en a pas encore est invisible à la comparaison — donc les deux ensembles coïncidaient réellement |

**Les trois preuves qui ont tranché, et aucune ne vient d'Anki :**

```bash
grep -c '<!--ID: ' Lexique/*.md                   # → 0 : rien n'a été écrit en retour
python3 -c "import json,io; d=json.load(io.open('.obsidian/plugins/\
obsidian-to-anki-plugin/data.json')); print([k for k in d['File Hashes'] \
if 'Lexique' in k])"                              # → [] : le plugin n'a jamais lu ces fichiers
stat -c '%y' .obsidian/plugins/obsidian-to-anki-plugin/data.json
                                                  # → antérieur au scan : le plugin n'a pas sauvegardé
```

> **`File Hashes` est le meilleur témoin du dispositif.** Le plugin y inscrit une
> empreinte par fichier **lu**. Un fichier absent de cette table n'a pas été analysé —
> ce qui distingue *« le scan a échoué sur cette carte »* de *« le scan n'a jamais vu ce
> fichier »*. Les deux pannes se ressemblent côté Anki et n'ont pas le même remède.

**Le correctif appliqué :** `orphelines.py` ne dit plus `✅` quand des cartes attendent
un identifiant. Il distingue désormais *« ça coïncide et rien n'attend »* de *« ça
coïncide, mais 14 cartes n'ont pas d'identifiant »*. **Un contrôle qui ne peut pas voir
quelque chose doit le dire, pas afficher une coche.**

## Combien de cartes sont en jeu aujourd'hui

**Compter les identifiants, pas les questions** — il y a deux syntaxes de carte :

```bash
grep -rhc '<!--ID: ' --include='*.md' Esprit Social Tech Corps Lexique Drills \
  | awk '{s+=$1} END {print s}'
```

Ce nombre doit égaler celui des notes Anki après chaque scan — c'est le contrôle
d'alignement ci-dessus.

> ⚠️ **Ne pas compter `^Q: `.** Les fiches `Vocab-` emploient la syntaxe
> `mot :: définition`, qui produit deux cartes par ligne et ne contient aucun `Q:`.
> Le 2026-10-03, compter les questions sous-estimait de **12 cartes** et aurait fait
> croire à douze orphelines. L'identifiant, lui, est écrit par le plugin quelle que
> soit la syntaxe.

> ⚠️ **Ce n'est plus le signal de découpe.** La règle des 3 cartes mesurait la
> discipline du rédacteur et non l'atomicité de la note : elle ne s'est jamais
> déclenchée. Corrigée le 2026-09-30 — le signal est la longueur de la section
> `## L'idée`, et l'audit l'échantillonne. Voir décision 01 de [[Guide-Conventions]].

### 🔗 Connexions
* [[Guide-Conventions]] — *décision 01 pour l'atomicité, 05 pour le barème, 08 pour les cartes.*
* [[Guide-Reprise]] — *l'état du vault et les pièges rencontrés.*
* [[Concept-Active_Recall]] · [[Concept-Répétition_Espacée]] — *les deux dispositifs qui justifient tout ceci.*
* [[MOC-Audit]] — *les notes sans carte, et le reste des dettes.*
