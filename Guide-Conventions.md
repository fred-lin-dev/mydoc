---
tags: [meta/guide, meta/ref]
---
# ⚖️ Conventions du vault

*Le contrat. Toute note créée dans ce vault s'y conforme, sans exception.
Référence de la méthode et du raisonnement : [[Guide-Méthode_Zettelkasten]].*

État : **Parties I à III tranchées** — les quatre décisions irréversibles (02, 03,
05, 08) sont figées. Reste la Partie IV (périmètre), modifiable à tout moment.

---

## 01 · Grain — une idée par note ✅

**Critère d'entrée : la citabilité.** Une idée mérite sa note si elle peut être
citée depuis un *autre domaine* que celui où elle a été rencontrée.

**Signal de découpe : la règle des 3 cartes.** Si une note réclame plus de trois
cartes de révision *sur des angles différents*, elle contient plus d'une idée →
la scinder. Le test ne coûte rien : il se déclenche sur un travail déjà fait (08).

---

## 02 · Nommage ✅

**Séparateurs — chaque caractère a un rôle unique, jamais l'autre :**

| Caractère | Rôle |
|---|---|
| `-` | sépare le préfixe de type du titre — **une seule fois, jamais dans le titre** |
| `_` | sépare les mots du titre |

```
Concept-Habitude_Atomique.md
Source-Atomic_Habits.md
MOC-Productivité.md
```

Bénéfice : `Source-Atomic_Habits` ↔ `Atomic_Habits.pdf` est une transformation
mécanique, donc scriptable sans cas particulier.

**Les cinq préfixes de type :**

| Préfixe | Contenu | Champ `fiabilite` ? |
|---|---|---|
| `Concept-` | note atomique — **une** idée | oui, obligatoire |
| `Source-` | fiche de livre ou d'article — mince | non |
| `MOC-` | index de domaine | non |
| `Ref-` | référence stable : barème, tableau, liste consultée | non |
| `Guide-` | procédure, workflow | non |

---

## 03 · Tags ✅

**Deux niveaux — `domaine/sous-domaine` — plus l'espace `meta/`.**

Le premier niveau duplique le dossier : redondance assumée. C'est le **second**
qui porte l'information qu'un dossier ne peut pas donner.

| Domaine | Sous-domaines ouverts |
|---|---|
| `esprit/` | `psychologie` `biais` `philosophie` `stratégie` `productivité` `habitudes` |
| `social/` | `influence` `négociation` `séduction` `style` `charisme` |
| `tech/` | `programmation` `outils` |
| `langues/` | `anglais` `vocabulaire` |
| `meta/` | `source` `moc` `ref` `guide` |

```yaml
tags: [esprit/habitudes, esprit/psychologie]   # une note atomique
tags: [meta/source, esprit/habitudes]          # une fiche de livre
tags: [meta/moc, social/séduction]             # un index
```

**Gouvernance — la règle des 5.** Un nouveau sous-tag ne se crée qu'à partir du
moment où **cinq notes** le justifient. En dessous, un tag existant plus large
fait l'affaire. Vaut aussi pour les domaines de premier niveau : `corps/`
(entraînement, nutrition, sommeil) naîtra à la 5ᵉ note de physiologie — d'ici là
`Why_We_Sleep` reste non fiché.

**Interdit :** tout tag terminé par `/` — c'est un placeholder de template oublié.
Contrôle d'audit obligatoire, parce que l'erreur est invisible à la lecture.

---

## 04 · Les index n'expliquent jamais ✅

Un `MOC-` **liste et qualifie d'une ligne**. Aucun savoir propre, **aucune carte
de révision** — règle absolue.

Raison : un index qui explique duplique les notes qu'il indexe, et la duplication
descend jusqu'aux cartes, où deux cartes posent la même question avec des réponses
divergentes. Indiagnostiquable après coup.

Contrôle d'audit : une syntaxe de carte dans un fichier `MOC-` = erreur.

---

## 05 · Champs de fiabilité ✅

**Les noms de champs sont figés** — ce sont eux qui rendent les notes
interrogeables, et les renommer plus tard invalide toutes les requêtes :

```yaml
source: "[[Source-Atomic_Habits]]"
fiabilite: 🟠 contesté
fiabilite_note: "Lally 2010, Eur J Soc Psychol 40(6), N=96, médiane 66j,
  IC 18-254j — le « 21 jours » est un mythe de vulgarisation"
```

**Le barème — cinq valeurs, écrites exactement comme suit :**

| Valeur | Signifie | `fiabilite_note` |
|---|---|---|
| `🟢 solide` | réplications convergentes, effet net | **obligatoire** — référence + chiffres |
| `🟠 contesté` | effet réel mais exagéré, ou débat ouvert | **obligatoire** — dire *ce qui* est contesté |
| `🔴 réfuté` | réfuté par réplication ou méta-analyse | **obligatoire** — la réfutation |
| `⚪ non évalué` | dette assumée, pas encore vérifié | vide |
| `⬜ non applicable` | la note n'affirme rien d'empirique | la vraie source (doc, définition) |

**La règle qui va avec.** Jamais « prouvé », « démontré » ou « validé
scientifiquement » sans référence à côté. Si on ne peut pas vérifier, on écrit
« non vérifié ». Un verdict sans sa référence est un avis, pas une information.

**Le champ est toujours présent sur un `Concept-`.** Jamais absent : un champ
absent est indistinguable d'un champ oublié, et l'audit ne peut plus rien en dire.

---

## 06 · Valeur par défaut ✅

**Un concept peut entrer sans verdict** — avec `⚪ non évalué`, explicitement.

Pourquoi : la vérification coûte 20 min à 1 h par concept, et sur du corpus
grand public **un tiers seulement survit intact**. Exiger le verdict avant
l'écriture, c'est ne rien écrire.

C'est donc une **dette assumée et mesurable**. La file de travail est une
requête d'une ligne, et elle se paie par **ordre d'utilité** — tri par nombre de
liens entrants — jamais par ordre d'arrivée.

---

## 07 · Ce qui échappe au verdict ✅

**Par valeur déclarée, jamais par domaine.** Aucune liste de domaines exemptés à
maintenir : la note dit elle-même qu'il n'y a rien à vérifier.

| Note | Verdict | Pourquoi |
|---|---|---|
| `Concept-Fold_Left` | `⬜ non applicable` | définition — vrai ou faux, vérifiable en 3 s |
| `Concept-Fenêtre_Anabolique` | `⚪ non évalué` | physiologie vulgarisée = dette, **pas** exemption |
| `Concept-Boucle_Habitude` | `🟢 solide` | affirmation sur le monde, réplications |

Conséquence : le cas limite du sport que le guide laisse ouvert est réglé sans
règle supplémentaire — ça ne dépend plus du dossier où la note vit.

**Le principe général qui gouverne l'audit :** quand une règle produit surtout
des faux positifs, **c'est la règle qu'on corrige, pas les notes**.

---

## 08 · Cartes de révision ✅

**Toutes les cartes en fin de note, sous un titre invariable `## 🎴 Cartes`.**
Deux lignes par carte, `Q:` puis `A:`, en début de ligne.

```markdown
## 🎴 Cartes

Q: Quelles sont les quatre phases de la boucle d'habitude ?
A: Signal → envie → réponse → récompense
<!--ID: 1727384950123-->

Q: Pourquoi « 21 jours pour une habitude » est-il faux ?
A: Lally 2010 : médiane 66 jours, IC 18-254 — la variance est le résultat
```

Pourquoi cette forme : `grep -c '^Q:'` donne le nombre de cartes, donc le
**signal de découpe de la décision 01 est mécanisable**. Plus de trois cartes sur
des angles différents → note candidate à la scission.

> ⚠️ **Les identifiants sont écrits par le plugin. Jamais à la main.**
> Un ID inventé fait échouer la synchronisation **en silence** : le plugin tente
> de mettre à jour une carte qui n'existe pas, échoue, et n'enregistre jamais le
> fichier. Des cartes peuvent rester bloquées des mois sans aucun signal.

**Decks — un sous-deck par domaine de premier niveau.** Le tag détermine le deck,
donc aucun choix à faire à la création :

```
esprit/…   → Zettelkasten::Esprit
social/…   → Zettelkasten::Social
tech/…     → Zettelkasten::Tech
langues/…  → Zettelkasten::Langues
```

Les sous-sous-decks naîtront avec la même **règle des 5**. Un deck à plat est
exclu : la même formulation peut avoir deux réponses justes selon le domaine.

**Les cartes sont tolérées en dette** — une note peut naître sans carte — *à
condition que l'audit les réclame*. Sans ça, la tolérance devient l'oubli.

---

## 09 · Audit ✅

Deux outils, parce que ce sont deux besoins différents :

| Outil | Rôle | Quand |
|---|---|---|
| `MOC-Audit.md` — Dataview | ce qui se lit dans le frontmatter : dette de fiabilité triée par liens entrants, livres sans note atomique, notes orphelines, notes sans carte | **en direct**, visible pendant le travail |
| `Scripts/audit.py` | ce que Dataview ne voit pas : liens morts, doublons de nom, frontmatter YAML cassé, sections absentes, restes de template, tags terminés par `/` | lancé à la main |

**La règle de conception : le script ne modifie rien.** Il produit un rapport. La
correction est une décision, et une décision ne s'automatise pas — le *constat*, si.

**Et le script se vérifie lui-même.** Une expression régulière trop stricte peut
ignorer des dizaines de notes qui ont pourtant le problème. Son compteur n'est pas
une vérité : le relire de temps en temps sur un échantillon lu à la main.

---

## 10 · Renommage ✅ *(contrainte d'outil, rien à trancher)*

**Jamais de `mv` depuis le terminal. Toujours F2 dans Obsidian.**

Obsidian ne met à jour les liens entrants que lors d'un renommage fait *dans*
Obsidian. Un `mv` casse tous les liens entrants sans aucun message, et la casse ne
se détecte qu'au prochain audit — quand on ne sait plus ce qui a été renommé.

C'est la seule règle absolue du vault. Elle s'applique aussi à moi, Claude : je ne
renomme ni ne déplace jamais un `.md` par le shell.

---

## 11 · Point d'entrée et garde-fou ✅

**Entrée par le livre.** Le PDF est la matière première : on lit, on extrait, la
fiche `Source-` reste **mince** (métadonnées, thèse en une ligne, analyse perso,
actions). Le savoir vit dans les `Concept-`, jamais dans la fiche.

```
Extras/Books/…/Atomic_Habits.pdf
  → Source-Atomic_Habits.md          (mince)
    → Concept-Boucle_Habitude.md      (le savoir)
    → Concept-Quatre_Lois_Habitude.md
    → Concept-Empilement_Habitudes.md
```

> ⚠️ **Le risque de cette porte est comportemental, pas structurel :** le
> **collector's fallacy** — accumuler des livres en croyant accumuler du savoir.

**Le garde-fou, contrôlé par l'audit : un livre fiché doit produire au moins une
note atomique.** Une `Source-` sans aucun `Concept-` lié est signalée.

Le taux de conversion est la métrique qui compte, et elle est mesurable :

| Compteur | Aujourd'hui |
|---|---|
| PDF dans `Extras/` | 37 |
| fiches `Source-` | 0 |
| fiches ayant produit ≥ 1 `Concept-` | 0 |

L'écart entre ces trois chiffres dit exactement combien de lecture a été convertie.

---

## 12 · Le périmètre — trois niveaux ✅

Ce n'est pas « fiché ou dehors ». C'est :

| Niveau | Fiche `Source-` | Notes `Concept-` | Champ `source` des notes |
|---|---|---|---|
| **Fiché** — livre d'idées prescriptif | oui, complète | oui | `Source-<titre>` |
| **Lu sans fiche** — manuel, cahier d'exercices, texte primaire | **non** | oui | le PDF directement |
| **Dehors** — fiction de loisir, livre écarté après examen | non | non | — |

**Les livres au niveau « lu sans fiche » :** Modern Compiler Implementation in ML,
The Pragmatic Programmer, English Phrasal Verbs in Use, Stage Academy Workbook,
Critique of Pure Reason, Beyond Good and Evil, Meditations, The Prince, The Art of War.

Raison : « thèse en une ligne » et « actions concrètes » n'ont aucun sens pour un
manuel de compilation ou pour Kant. Exiger la fiche produirait du remplissage.

**Les livres « dehors » :** To Kill A Mockingbird *(fiction de loisir)*. Et tout
livre **explicitement écarté** après examen — le ficher contredirait la décision
de l'écarter.

**Conséquence pour l'audit :** le garde-fou de 11 ne s'applique **qu'au niveau
fiché**. Les deux autres niveaux ne génèrent aucun faux positif. Sans ce
découpage, l'audit crierait sur dix livres qui n'ont rien de fautif — et un audit
qui crie pour rien cesse d'être lancé.

---

---

## 13 · Arborescence et langue *(hors guide — modifiable à tout moment)*

**Les dossiers dupliquent le premier niveau de tag.** Concepts et fiches
cohabitent dans le domaine : le préfixe suffit à les distinguer.

```
Esprit/  Social/  Tech/  Langues/   le savoir
Meta/                               MOC-Audit, Ref-Périmètre_Bibliothèque
Templates/                          les 5 modèles — exclus de l'audit
Scripts/                            audit.py
Extras/Books/                       les PDF
Guide-Conventions.md                ↰ la constitution reste à la racine,
Guide-Méthode_Zettelkasten.md       ↲ visible en premier
```

`Template-` est un sixième préfixe, réservé à `Templates/`. Ce n'est pas un type
de note : ces fichiers ne sont ni indexés ni audités.

**Langue : concepts en français, fiches de source en anglais.**

| | Exemple |
|---|---|
| `Concept-` | `Concept-Boucle_Habitude` — tu cherches dans la langue où tu penses |
| `Source-` | `Source-Atomic_Habits` — **le titre exact du livre**, c'est ce qui garde la correspondance avec `Atomic_Habits.pdf` mécanique |
| `MOC-` `Ref-` `Guide-` | français |

**L'exception :** quand le terme anglais *est* le terme du métier, on le garde —
`Concept-Call_Stack`, pas `Concept-Pile_Appels`. Le test : « est-ce que je le
dirais en français à voix haute ? » Non → on garde l'anglais.

Accents conservés dans les noms de fichiers.

---

## Plugins — en place

| Plugin | Version | Rôle |
|---|---|---|
| **Templates** *(cœur)* | — | insère les 5 modèles ; dossier réglé sur `Templates/` |
| **Dataview** | récupéré de l'ancien vault | les six tableaux de [[MOC-Audit]] |
| **Obsidian_to_Anki** | 3.6.0, récupéré de l'ancien vault | synchronise `## 🎴 Cartes` vers Anki |

Obsidian_to_Anki n'est plus distribué dans le navigateur de plugins : il a été
copié depuis `~/olddy`, avec sa configuration **réécrite** pour la syntaxe `Q:`/`A:`
et les decks `Zettelkasten::<Domaine>`. Procédure complète et pièges :
[[Guide-Anki_Workflow]].

> ⚠️ **Reste à faire au premier lancement :** activer les deux plugins dans Obsidian
> (*Paramètres → Modules tiers*), ouvrir Anki, puis `Scan Vault`. La liste de
> contrôle du premier scan est dans [[Guide-Anki_Workflow]].

---

### 🔗 Connexions
* [[Guide-Méthode_Zettelkasten]] — *le raisonnement derrière chaque décision.*
* [[MOC-Audit]] — *le tableau de bord qui contrôle ces règles.*
* [[Ref-Périmètre_Bibliothèque]] — *le niveau de périmètre de chaque PDF.*
