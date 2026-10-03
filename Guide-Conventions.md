---
tags: [meta/guide, meta/ref]
---
# ⚖️ Conventions du vault

*Le contrat. Toute note créée dans ce vault s'y conforme, sans exception.
Référence de la méthode et du raisonnement : [[Guide-Méthode_Zettelkasten]].*

> 🧭 **Tu reprends le travail après une interruption ?** Lis
> [[Guide-Reprise]] d'abord : état, constats et pièges rencontrés.

État : **Parties I à III tranchées** — les quatre décisions irréversibles (02, 03,
05, 08) sont figées. Reste la Partie IV (périmètre), modifiable à tout moment.

---

## 01 · Grain — une idée par note ✅

**Critère d'entrée : la citabilité.** Une idée mérite sa note si elle peut être
citée depuis un *autre domaine* que celui où elle a été rencontrée.

**Signal de découpe.** Une note qui porte plus d'une idée doit être scindée. Reste
à savoir comment on s'en aperçoit — et la première réponse était fausse.

### ⚠️ La règle des 3 cartes était un instrument mort — corrigé le 2026-09-30

Le signal d'origine était `grep -c '^Q:' > 3` : plus de trois cartes sur des angles
différents → scinder. Mesuré sur 137 notes :

```
cartes par note :   3 → 118 notes     2 → 19 notes     4 ou plus → 0
```

**Il ne s'est jamais déclenché et ne pouvait pas se déclencher.** Le nombre de
cartes est un **choix du rédacteur**, pas une propriété de la note : celui qui les
écrit s'arrête à trois parce que la règle dit trois. La règle mesurait sa propre
observance. C'est le pire état pour un contrôle — il a l'air vivant.

La règle reste en place comme **contrôle secondaire** : elle deviendrait informative
si des cartes étaient ajoutées à la main sans penser à la scission. Mais elle n'est
plus le signal.

### Le signal réel : la longueur de la section `## L'idée`

`audit.py` mesure les **mots de prose de la seule section `## L'idée`** — tableaux,
citations et blocs de code retirés, sinon on mesure la mise en forme.

**Pourquoi cette section et pas la note entière :** une longue section
« Ce qui la rend vraie, ou fragile » est un **bon** signe, c'est de la vérification.
Une longue idée en est un mauvais. Mélanger les deux annulait le signal.

**Le titre tolère un complément** — `## L'idée — telle qu'elle circule`,
`— telle que le livre la présente`. Sept notes l'emploient pour marquer qu'elles
exposent une thèse avant de la réfuter. Un contrôle strict aurait puni la rigueur.

**Ce n'est pas un verdict, c'est un échantillon.** Le seuil est le 9ᵉ décile de la
distribution courante, donc le contrôle renvoie toujours environ un dixième des
notes — c'est son objet. Il choisit l'échantillon que la **décision 09** demande de
relire à la main, au lieu de le tirer au hasard. Aucun compteur ne sait dire si une
note porte deux idées ; celui-ci sait dire lesquelles valent d'être relues d'abord.

**Vérifié dans les deux sens le jour de son ajout :** sur deux notes signalées,
`Concept-Terrain_Avant_Force` a été **gardée** après relecture — une seule thèse, sa
preuve textuelle et sa généralisation — et `Concept-Apparences_Normales` a été
**scindée**, un mécanisme général y étant enterré sous un cas particulier
([[Concept-Signal_Par_L_Absence]]). Un contrôle qui ne produirait que des scissions
serait aussi faux que celui qui n'en produit aucune.

### `atomicite_relue` — pour que la file puisse se vider

Le seuil étant relatif, le contrôle renverrait **toujours** un dixième des notes. Sans
mémoire, la file ne se viderait jamais et une séance de relecture ne laisserait **aucune
trace** — la suivante relirait les mêmes notes. C'était le défaut miroir de la règle des
3 cartes : une file infinie vaut une règle muette.

D'où un champ, sur le modèle de `fiabilite_date` :

```yaml
atomicite_relue: 2026-10-01
```

**L'audit ne signale qu'une note du dernier décile qui ne le porte pas.** Le champ
n'affirme pas que la note est atomique pour toujours — il dit qu'elle a été **jugée
telle à cette date**, par quelqu'un qui l'a lue en entier.

**Première passe complète le 2026-10-01 :** 14 notes signalées, 14 relues, **16 marquées**
(les deux notes nées des scissions comprises). Résultat : **12 gardées, 2 scindées** —
[[Concept-Erreur_Ludique]] détachée de `Concept-Cygne_Noir`, et
[[Concept-Sens_Par_L_Engagement]] détachée de `Concept-Sens_Comme_Ressource`. Dans les
deux cas **j'avais signalé la couture en écrivant la note** : « que Taleb range ici », « et
le second point ». Le signal n'a rien découvert que le texte ne disait pas — il a dit
**où regarder**.

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

**Les six préfixes de type :**

| Préfixe | Contenu | Champ `fiabilite` ? | Produit des cartes ? |
|---|---|---|---|
| `Concept-` | note atomique — **une** idée | oui, obligatoire | oui, `Q:`/`A:` |
| `Source-` | fiche de livre ou d'article — mince | non | non |
| `MOC-` | index de domaine | non | **interdit** (décision 04) |
| `Ref-` | référence stable : barème, tableau, liste **consultée** | non | non |
| `Guide-` | procédure, workflow | non | non |
| `Vocab-` | fiche de vocabulaire — liste **apprise** | non | oui, `Vocabulaire_Elite` |

> **Pourquoi un sixième préfixe, ajouté le 2026-10-03.** Une fiche de vocabulaire
> n'entrait dans aucun des cinq. Ce n'est pas une thèse, donc pas un `Concept-` : un mot
> ne s'évalue pas au barème, il se définit. Et ce n'est pas une `Ref-`, dont la
> définition même est *« consultée, pas apprise »* — alors qu'une liste de mots n'a
> d'intérêt que **mémorisée**. La ligne de partage entre `Ref-` et `Vocab-` est donc
> exactement celle-là : **produit-elle des cartes ?**
>
> **Conséquence sur le type Anki, et c'est le vrai motif :** `Vocab-` n'emploie pas
> `Q:`/`A:` mais le type `Vocabulaire_Elite`, qui génère **deux cartes par mot** — dont
> une dans le sens *définition → mot*. C'est le seul sens qui rend plus articulé, et il
> est impossible à obtenir avec le type `Basic`. Voir [[Guide-Anki]].

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
| `corps/` | `sommeil` `santé` |
| `meta/` | `source` `moc` `ref` `guide` |

```yaml
tags: [esprit/habitudes, esprit/psychologie]   # une note atomique
tags: [meta/source, esprit/habitudes]          # une fiche de livre
tags: [meta/moc, social/séduction]             # un index
```

**Gouvernance — la règle des 5.** Un nouveau sous-tag ne se crée qu'à partir du
moment où **cinq notes** le justifient. En dessous, un tag existant plus large
fait l'affaire.

### Le seul sous-dossier de domaine autorisé — `Langues/`, 2026-10-03

**La règle générale ne change pas : les dossiers de domaine sont plats.** Un
sous-dossier qui encoderait la taxonomie serait une seconde copie des tags, et le vault
en a déjà supprimé un pour cette raison — `Extras/Books/Soft/`.

`Langues/` est l'exception, et elle tient à une raison qu'aucun autre domaine n'a :
**la langue n'est pas un sous-domaine, c'est une partition.** Une note de `social/` peut
appartenir à deux sous-domaines ; un mot appartient à une langue et à une seule. Et
surtout, **la langue doit séparer les decks Anki** — réviser du vocabulaire français et
anglais dans le même paquet mélange deux exercices différents.

```
Langues/MOC-Langues.md            l'index, au niveau du domaine
Langues/Français/                 → deck Zettelkasten::Langues::Français
```

> ⚠️ **Deux conséquences mécaniques, les deux vérifiées le 2026-10-03.**
> 1. **Le plugin Anki résout le deck sur le chemin exact du dossier, il ne remonte pas
>    au parent.** `Langues/Français` a donc besoin de sa **propre** entrée dans
>    `FOLDER_DECKS`, sans quoi ses cartes tombent dans le deck par défaut.
> 2. **Les scripts doivent parcourir en `rglob`, pas en `glob`.** Dans
>    `Scripts/orphelines.py` l'oubli n'aurait pas produit un chiffre faux : les
>    identifiants du sous-dossier auraient été absents de l'ensemble du vault, donc
>    **comptés comme orphelins**, et ce script imprime une commande `deleteNotes`.

> ✅ **La règle a fonctionné une fois, et c'est son premier test réel.** `corps/`
> était annoncé et vide depuis le premier jour. Il est né à la phase 5, quand
> *Why We Sleep* et *The Body Keeps the Score* ont produit **exactement cinq** notes
> de physiologie — pas avant, et sans qu'on ait eu à décider.

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
fiabilite_date: 2026-09-28
```

**Le barème — six valeurs, écrites exactement comme suit :**

| Valeur | Signifie | `fiabilite_note` |
|---|---|---|
| `🟢 solide` | réplications convergentes, effet net | **obligatoire** — référence + chiffres |
| `🟠 contesté` | effet réel mais exagéré, ou débat ouvert | **obligatoire** — dire *ce qui* est contesté |
| `🔴 réfuté` | réfuté par réplication ou méta-analyse | **obligatoire** — la réfutation |
| `⚪ non évalué` | dette assumée, pas encore vérifié | vide |
| `⬜ non applicable` | la note n'affirme rien d'empirique | la vraie source (doc, définition) |
| `🔵 invérifiable` | **examinée, et rien ne permet de trancher** | **obligatoire** — ce qui a été cherché, et ce qu'il faudrait |

### La sixième valeur — `🔵 invérifiable`, ajoutée le 2026-10-02

**Elle existe parce que `⚪` en disait deux choses incompatibles :** « pas encore
examiné » et « examiné, et rien ne permet de trancher ». La seconde restait dans la file
de dette, où quelqu'un la réexaminait — c'est-à-dire refaisait un travail déjà fait, sans
le savoir.

Les trois valeurs voisines se distinguent par **ce qu'on a fait et ce qui existe** :

| | On a cherché ? | Y a-t-il quelque chose à trouver ? |
|---|---|---|
| `⚪ non évalué` | **non**, c'est une dette | peut-être |
| `🔵 invérifiable` | **oui** | non, pas en l'état |
| `⬜ non applicable` | sans objet | **rien** — la note n'affirme rien d'empirique |

**`🔵` vieillit comme un verdict tranché**, et c'est le point de conception qui le
justifie : il porte une `fiabilite_note` disant **ce qui a été cherché et ce qu'il
faudrait** pour trancher, plus une `fiabilite_date`. Au-delà de l'horizon, l'audit le
rouvre — parce qu'une littérature peut être parue entre-temps. Un `⬜`, non : une
définition ne devient pas fausse avec le temps.

**Les quatre premières, le jour de son introduction :** `Structure_Ascendante`,
`Réserve_De_Matière`, `Paradoxe_Du_Succès`, `Apparences_Normales` — les quatre dernières
dettes d'une file de 42, examinées sans qu'aucune littérature ne permette de les
trancher. Chacune dit dans sa justification quelle étude il faudrait.

### `fiabilite_date` — un verdict se périme, ajouté le 2026-09-30

**Obligatoire sur `🟢`, `🟠`, `🔴` et `🔵`, absent de `⚪` et `⬜`.** L'audit refuse un
verdict daté sans date, au même titre qu'il refuse un verdict sans référence.

**Pourquoi ces quatre :** chacun dépend d'un **état de la littérature**, et cet état a
une date — y compris `🔵`, qui dit « rien ne permettait de trancher **à cette date** ».
Une définition `⬜` ne vieillit pas, et un `⚪` est déjà une dette.

**Horizon : 24 mois.** L'ordre de grandeur auquel une méta-analyse ou une
réplication large peut renverser une conclusion. Au-delà, l'audit remet le verdict
en dette — il ne le supprime pas, il le rouvre.

L'en-tête du rapport porte toujours l'âge du verdict le plus ancien et le nombre de
verdicts à moins de six mois de l'échéance, **pour que le contrôle ne soit jamais
muet** avant de se déclencher.

> ⚠️ **Ce qui distingue ce délai d'un quota.** La règle des 3 cartes ne pouvait pas
> se déclencher, parce qu'elle mesurait la discipline de celui qui écrivait
> (décision 01). Celle-ci **se déclenchera toute seule, par le passage du temps**,
> sans dépendre de personne. C'est le seul contrôle du vault dont le déclenchement
> ne soit pas conditionné à un comportement.

**Les 45 verdicts existants ont été datés depuis l'historique git** — date de
première apparition du fichier, pas une date inventée : 15 au 2026-09-27, 27 au
2026-09-28, 3 au 2026-09-29.

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
| `Concept-Erreur_De_Planification` | `🟢 solide` | affirmation sur le monde, réplications |

> ⚠️ **Cette dernière ligne citait `Concept-Boucle_Habitude` jusqu'au 2026-10-01**, alors
> que cette note dit d'elle-même être « une taxonomie descriptive, pas une théorie
> testable » — soit la définition de `⬜`. **L'exemple de la constitution contredisait la
> note qu'il citait.** Trouvé en payant la dette, pas par un contrôle : aucun script ne
> peut vérifier qu'une illustration est bien choisie.

Conséquence : le cas limite du sport que le guide laisse ouvert est réglé sans
règle supplémentaire — ça ne dépend plus du dossier où la note vit.

**Le principe général qui gouverne l'audit :** quand une règle produit surtout
des faux positifs, **c'est la règle qu'on corrige, pas les notes**.

### Les index sont contrôlés contre les notes — ajouté le 2026-10-01

Un `MOC-` est un index (décision 04) : **un index qui omet des entrées ne fait pas son
travail, et un index qui annonce un faux verdict désinforme.** L'audit compare donc chaque
`Concept-` à la ligne qui le liste dans le `MOC-` de son domaine :

| Écart | Gravité |
|---|---|
| note absente de son index | **alerte** |
| l'index annonce un verdict différent de la note | **erreur** — il affirme quelque chose de faux |
| les compteurs de l'en-tête ne correspondent pas | **alerte** |

**Le verdict apparaît donc à deux endroits** — dans la note et dans son index — ce qui est
la duplication que la décision 12 interdit pour les niveaux de périmètre. La différence
est qu'**ici un contrôle la garde** : les niveaux avaient divergé précisément parce que
rien ne les comparait. Une duplication gardée n'est pas du même ordre qu'une duplication
libre, et l'emoji en tête de ligne a une valeur de lecture que Dataview ne remplace pas.

**Pourquoi ce contrôle existe :** trois dérives de ce genre ont été trouvées **à la main**
avant lui — des compteurs périmés, `Corps/` absent des cinq requêtes Dataview, et
**une section entière de quatre notes jamais ajoutée à `MOC-Social`**. Un artefact tenu à
la main dérive de ce qu'il décrit, silencieusement, et c'est la seule classe de défaut qui
s'est répétée.

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

### Règle d'autonomie — une carte se révise sans sa note

**La question doit nommer son sujet.** En révision, Anki tire les cartes dans le
désordre : la note n'est pas là, la carte précédente non plus. Tout ce que la
question désigne sans le nommer n'a plus de référent.

Deux formes sont donc interdites :

| Interdit | Pourquoi |
|---|---|
| **démonstratif sans référent** — « ce principe », « cette règle », « cet effet » | rien dans la carte ne dit de quoi il s'agit |
| **« le livre », « l'auteur », « cette note »** | l'ouvrage se nomme ; et une carte ne parle jamais du vault, elle parle du monde |

Le champ `Source` du plugin **ne répare rien** : il est au dos de la carte, donc
visible seulement après la réponse.

**Le correctif est un préfixe**, repris mot pour mot du titre H1 de la note :

```markdown
Q: **Engagement et cohérence** — quelle est la défense contre ce levier ?
A: Repérer la demande minuscule qui précède la vraie, et se rappeler que rien
   n'oblige à être cohérent avec un engagement obtenu par surprise.
```

**Le préfixe ne se met pas partout.** Une question qui nomme déjà son sujet n'en
a pas besoin, et l'ajouter serait nuisible : sur une carte de définition, le titre
**souffle la réponse**. `**Active recall** — qu'est-ce qui consolide une
information : la réexposition ou la récupération ?` donne le résultat avant la
question. Donc : *préfixe si et seulement si la question ne se suffit pas.*

**La pratique est détaillée dans [[Guide-Anki]], partie 1** — le principe de
la limite, la forme du trio, et les pièges de rédaction.

Le test est une lecture à voix haute de la seule ligne `Q:`, sans rien d'autre
sous les yeux. L'audit signale les démonstratifs sans référent, mais il ne
remplace pas ce test — il ne sait pas lire une question.

### Les deux faces, et le vocabulaire du vault — ajouté le 2026-10-03

Après relecture des **466 cartes une par une** dans Anki, trois défauts sont
apparus que le contrôle ne pouvait pas voir, et **deux d'entre eux étaient dans
des réponses** — il ne lisait que les questions. Il lit maintenant les deux faces.

**Une carte parle du monde, jamais du vault.** Le vocabulaire interne est désormais
refusé des deux côtés :

| Refusé | Pourquoi |
|---|---|
| `vault`, `le corpus` | ne désignent rien pour qui révise |
| `le verdict`, et les cinq symboles 🟢 🟠 🔴 ⚪ ⬜ | le barème de la décision 05 est une convention d'ici |
| `les auteurs` non suivi de « de » | l'ouvrage se nomme, comme pour « le livre » |

Les cinq cartes fautives disaient par exemple *« sur quoi repose son verdict 🟢 »*
ou *« quel autre cas de dose ronde le vault porte-t-il »*. Une question sur le
classement d'une note n'est pas une question sur le monde.

### Une page citée dans une carte porte son ouvrage — ajouté le 2026-10-03

Seize cartes citaient `(p. 61)`, `(p. 113)` sans nommer le livre. Lue seule, une
page nue est **l'ordre d'aller vérifier ce qu'on ne peut pas localiser** — le pire
état pour un vault dont la méthode repose sur la citation vérifiable.

**Forme attendue : `(*Titre*, p. N)`.** L'audit refuse toute parenthèse de page qui
ne commence pas par un titre en italique. Les repères canoniques d'une autre nature
— `(B 19)` pour Kant, `(A 421 / B 449)` — ne sont pas concernés : ils identifient
l'édition par eux-mêmes.

### La réponse doit être vérifiable — ajouté le 2026-10-02

**Une question qui réclame un item abstrait sans nommer ses candidats n'a pas de critère
de réussite.** On ne peut pas savoir si ce qu'on a trouvé compte.

```
✗  quelle nuance le livre escamote-t-il ?          dix réponses défendables
✓  relire en méthode principale, ou après un       deux candidats nommés,
   échec de rappel : le livre distingue-t-il ?     la réponse se vérifie
```

**Le correctif est toujours le même : nommer les candidats dans la question.** Le plus
souvent ça donne un choix binaire, et c'est une amélioration et non un appauvrissement —
une carte qu'on ne peut pas corriger ne mesure rien.

L'audit signale ces questions en **info**, parce que le repérage est heuristique et que la
réécriture est une décision. Une question signalée mais jugée acceptable s'exempte par
`cartes_relues: AAAA-MM-JJ` dans le frontmatter de la note.

> **D'où vient cette règle.** Yinpi a marqué trois cartes d'un drapeau en révision, avec
> un diagnostic précis : *« pour le trauma, laquelle ne suit pas ? c'est écrit nulle
> part »*. La réponse listait trois affirmations avec des étiquettes entre parenthèses et
> ne désignait jamais celle qu'on demandait. **Ni l'audit ni Claude ne pouvaient trouver
> ça** — seule la révision le pouvait.
>
> ⚠️ Et le contrôle a été écrit **deux fois** : le premier motif employait `quelle?`, qui
> signifie « quell » ou « quelle » et **jamais « quel »**. Il laissait donc passer la
> moitié des cas, dont les trois cartes fautives que Claude venait d'écrire lui-même.
> Mesure corrigée : **8 % du corpus antérieur**, contre 4 % annoncés d'abord.

### ⚠️ Une carte neuve se met **en dernier**, jamais au milieu

**Le plugin apparie les identifiants aux cartes par ordre d'apparition, pas par
adjacence** — le n-ième identifiant du bloc va à la n-ième carte, où que le commentaire
soit écrit. Une carte sans identifiant placée ailleurs qu'en dernier **vole donc celui de
sa voisine**, et le scan suivant écrase une note Anki avec le mauvais contenu.

Ça s'est produit le 2026-10-02 et il a fallu trois scans pour le comprendre. **L'audit le
détecte désormais en erreur**, et hors réseau : un trou dans la suite des identifiants est
signalé avant qu'un scan puisse faire le dégât.

Si l'ordre logique veut qu'une carte neuve vienne avant les autres : l'écrire en dernier,
scanner, puis la remonter **avec son identifiant**. Détail et contrôle d'alignement dans
[[Guide-Anki]].

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

### L'exception, ajoutée le 2026-09-29

**Je peux `mv` ou `rm` un `.md` si, et seulement si, aucun fichier ne pointe vers
lui.** Sans lien entrant, il n'y a rien à casser, donc rien que F2 sache faire de
mieux. Le contrôle est mécanique et se fait **avant** l'opération :

```bash
grep -rc 'Nom_Du_Fichier' --include='*.md' . | grep -v ':0'
```

Une seule ligne attendue : le fichier lui-même. **Dès qu'il y en a une autre, je
n'agis pas et je demande** — c'est alors une décision de rangement, pas une
manipulation de fichier, et le cas du 2026-09-29 montre pourquoi : au renommage de
`Ref-Périmètre_Bibliothèque` en [[Ref-Bibliothèque]], Obsidian a réécrit les 13
liens `[[…]]` et **laissé les 4 mentions en texte brut** — dans un bloc de code, une
phrase, une case de tableau, une tâche. Même F2 ne fait pas tout.

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
Esprit/  Social/  Tech/  Corps/  Langues/     le savoir
         Langues/Français/                    ← le seul sous-dossier de domaine
Meta/        tout ce qui n'est pas du savoir :
             Guide-Reprise · Guide-Stratégie_Lecture · Guide-Anki
             MOC-Audit · Ref-Bibliothèque · les 3 Ref-Lecture_*
             ↑ l'inventaire des livres : niveau, domaine, possession — une seule fois
Templates/   les 5 modèles — exclus de l'audit et du scan Anki
Scripts/     audit.py · orphelines.py — les deux en lecture seule
Extras/Books/  les PDF, à plat

Guide-Conventions.md            ↰ la racine n'accueille QUE la constitution.
Guide-Méthode_Zettelkasten.md   ↲ Deux fichiers, visibles en premier.
```

> ⚠️ **Rien d'autre à la racine.** Tout `Ref-`, `MOC-` ou `Guide-` qui n'est pas la
> constitution va dans `Meta/`. Les trois listes de lecture y ont été déplacées le
> 2026-09-28 : elles étaient restées à la racine par inadvertance, à côté de
> `Ref-Bibliothèque` qui est le même genre d'objet et se trouvait déjà dans
> `Meta/`. Une incohérence de rangement est une fenêtre brisée au sens de
> [[Concept-Fenêtre_Brisée]].
>
> **Et pas de dossier hors domaine.** Un `Lecture/` serait tentant et faux : les dossiers
> reflètent le premier niveau de tag, `Meta/` étant l'unique exception assumée. En ajouter un
> troisième mécanisme de rangement viole [[Concept-Orthogonalité]] et défait la décision 03.

`Template-` est un sixième préfixe, réservé à `Templates/`. Ce n'est pas un type
de note : ces fichiers ne sont ni indexés ni audités.

> ⚠️ **`Extras/Books/` est plat, et doit le rester.** Aucun sous-dossier par domaine,
> par thème ou par statut de lecture.
>
> * Le domaine de chaque PDF est déjà dans [[Ref-Bibliothèque]], **source
>   autoritaire unique**. Une arborescence serait une seconde copie de la même
>   décision, et deux copies divergent — voir [[Concept-DRY]].
> * Aucune boîte de réception n'est nécessaire : un PDF sans niveau de périmètre est
>   **signalé en alerte par l'audit**. L'alerte est la boîte de réception, et elle ne
>   peut pas être oubliée.
> * Les liens des fiches sont par **nom** — `pdf: "[[Deep_Work.pdf]]"` — jamais par
>   chemin. Déplacer un PDF ne casse rien ; le **renommer** casse la fiche.
>
> *Le sous-dossier `Soft/` d'origine a été supprimé : il encodait la taxonomie
> fourre-tout que la décision 03a a écartée.*

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
[[Guide-Anki]].

> ⚠️ **Reste à faire au premier lancement :** activer les deux plugins dans Obsidian
> (*Paramètres → Modules tiers*), ouvrir Anki, puis `Scan Vault`. La liste de
> contrôle du premier scan est dans [[Guide-Anki]].

---

### 🔗 Connexions
* [[Guide-Méthode_Zettelkasten]] — *le raisonnement derrière chaque décision.*
* [[MOC-Audit]] — *le tableau de bord qui contrôle ces règles.*
* [[Ref-Bibliothèque]] — *l'inventaire : 84 titres, leur niveau, leur domaine,
  et s'ils sont sur le disque. Les `Ref-Lecture_*` n'en redisent rien.*
