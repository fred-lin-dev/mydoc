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
