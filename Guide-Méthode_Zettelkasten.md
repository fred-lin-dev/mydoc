---
tags: [meta/guide]
---
# 🗂️ Avant la première note — les douze décisions

*Document de travail, à relire à deux. Les décisions qu'il faut prendre avant
d'écrire quoi que ce soit dans un Zettelkasten : ce que chacune coûte, ce qu'elle
interdit, et lesquelles peuvent différer entre deux personnes sans casser la
possibilité de se relire.*

---

## Le problème qu'on essaie de résoudre

Un système de notes échoue toujours de la même façon : il grossit, et il devient
plus coûteux d'y retrouver une idée que de la rechercher ailleurs. Tout ce qui
suit n'existe que pour retarder ce moment.

Trois mécanismes le provoquent, et chacun appelle une décision structurelle :

* **Les notes deviennent des résumés.** Une note par livre, longue, exhaustive.
  Jamais relue, parce qu'elle ne répond à aucune question précise. → décisions 01 à 04.
* **Le savoir perd son origine.** Au bout d'un an, on ne sait plus si une affirmation
  vient d'une méta-analyse ou d'un thread Twitter. → décisions 05 à 07.
* **Le système se dégrade en silence.** Liens morts, doublons, conventions qui
  divergent. Rien ne prévient. → décisions 08 à 10.

Les douze décisions sont indépendantes. On peut en adopter neuf et en refuser
trois — mais il vaut mieux savoir lesquelles, parce que certaines se tiennent
par paires.

---

# Partie I — La structure

## 01. Le grain : une idée par note

La règle est facile à énoncer, difficile à appliquer. Le vrai test n'est pas la
longueur, c'est la **citabilité** :

> **Le test.** Cette idée peut-elle être citée depuis un *autre domaine* que celui
> où je l'ai rencontrée ?

Si oui, elle mérite sa note. Un concept de gestion du risque financier qu'on finit
par citer depuis la stratégie sociale *et* depuis l'entraînement a gagné son
autonomie — il n'appartient plus à son livre d'origine.

**Le coût.** Un grain trop fin produit des notes d'une ligne que personne ne relit.
Trop gros, des notes impossibles à relier : elles contiennent trop de choses pour
être citées précisément.

> **À trancher.** Adopter le même test tous les deux. Pas la même granularité —
> elle viendra naturellement — mais le même *critère*, sinon vos notes ne pourront
> pas se citer l'une l'autre.

---

## 02. Le type dans le nom du fichier

Préfixer chaque note par ce qu'elle est : note atomique, fiche de source, index,
référence stable, procédure. Le préfixe détermine aussi le template utilisé à la
création.

| Ce que ça donne | Ce que ça coûte |
|---|---|
| Le graphe devient lisible sans ouvrir les notes | Des noms longs |
| Le tri est trivial | La convention de casse devient irréversible en pratique |
| Un script peut appliquer des règles différentes par type | La changer après 300 notes est un chantier |

> ⚠️ **Le piège technique.** Choisir underscores **ou** tirets, jamais les deux.
> Les templates génèrent souvent des liens à partir du nom — `[[<nom>.pdf]]` par
> exemple. Un séparateur incohérent casse ces liens **en silence** : rien ne
> s'affiche en rouge, le lien pointe simplement vers rien.

> **À trancher.** La liste des préfixes, et la convention de séparateur. Premier
> jour, par écrit.

---

## 03. Les tags : ce qu'ils font que les dossiers et les liens ne font pas

C'est la décision la plus souvent bâclée, parce que les trois mécanismes se
recouvrent partiellement. La répartition qui tient :

| Mécanisme | Répond à | Cardinalité |
|---|---|---|
| **Dossier** | Où la note vit physiquement | Un seul |
| **Tag** | De quoi elle parle, en facettes interrogeables | Plusieurs |
| **Lien** | À quoi elle se rattache | Autant que nécessaire |

La taxonomie retenue ici est **hiérarchique à deux niveaux** — `domaine/sous-domaine` —
plus un espace de noms `meta/` pour ce qui n'est pas du savoir :

```yaml
tags: [esprit/psychologie, esprit/productivité]   # une note atomique
tags: [meta/source, esprit/productivité]          # une fiche de livre
tags: [meta/moc, corps/santé]                     # un index
tags: [lexique/français]                          # une fiche de vocabulaire
```

**Pourquoi deux niveaux et pas un.** Le premier niveau duplique le dossier
(`esprit/…` pour les notes dans `Esprit/`), et cette redondance est assumée : c'est le
**second** niveau qui porte l'information que le dossier ne peut pas donner.
`esprit/psychologie` et `esprit/productivité` vivent dans le même dossier — seul le tag
les sépare.

> ⚠️ **Corrigé le 2026-10-03 : ces exemples portaient `soft/` et `sport/`**, qui sont les
> domaines de l'**ancien** vault et n'ont jamais existé ici. La liste réelle est dans
> [[Guide-Conventions]], décision 03, et elle seule fait foi. **Aucun contrôle ne lit les
> fichiers `Guide-`** — c'est le troisième artefact rédigé à la main trouvé en décalage
> avec le vault, après le bloc d'état de [[Guide-Reprise]] et les niveaux de périmètre
> jamais relus. Et `meta/` traverse tous les dossiers, ce qu'un dossier ne sait pas faire.

**Pourquoi un espace `meta/`.** Le type de note est déjà dans le préfixe du nom.
Le tag `meta/` le rend *interrogeable en masse* : « toutes les fiches de source
sur la productivité » est une requête à une ligne, impossible avec les seuls
préfixes.

> ⚠️ **Le piège du placeholder.** Le template livre `tags: [soft/]` — un tag
> incomplet, à compléter à la création. Oublié, il produit un tag qui ne veut rien
> dire et pollue le panneau des tags. **Faire contrôler par le script tout tag qui
> se termine par `/`** : c'est un des contrôles les plus rentables, parce que
> l'erreur est invisible à la lecture.

**Le coût.** Une taxonomie qui grossit sans gouvernance devient du bruit : trente
sous-tags à trois notes chacun ne servent à rien. Règle simple : un nouveau
sous-tag ne se crée qu'à partir du moment où il a de quoi être utile — cinq notes
est un seuil raisonnable. En dessous, un tag existant plus large fait l'affaire.

> **À trancher.** La profondeur (un ou deux niveaux), la liste des domaines de
> premier niveau, et l'existence d'un espace `meta/`. C'est une des cinq
> conventions qui doivent être identiques pour que vous puissiez échanger des
> notes — voir la partie V.

---

## 04. L'index n'explique jamais

Les notes d'index — une par domaine, une par livre — listent et qualifient d'une
ligne. Elles ne contiennent aucun savoir propre.

**Pourquoi c'est strict.** Dès qu'un index se met à expliquer, il duplique les
notes qu'il indexe. Et la duplication ne s'arrête pas au texte : elle descend
jusqu'aux cartes de révision, où deux cartes finissent par poser la même question
avec des réponses légèrement différentes. Impossible à réviser, et très difficile
à diagnostiquer après coup.

> **À trancher.** Interdire les flashcards dans les index. Règle d'une ligne, elle
> supprime la cause mécanique du problème.

---

# Partie II — L'épistémique

*C'est la partie où une approche « science-based » se gagne ou se perd. Elle ne se
joue pas au moment de choisir les livres — elle se joue dans un champ du frontmatter.*

## 05. Un champ de fiabilité, avec sa justification

Chaque note atomique porte deux champs : un verdict et sa référence.

```yaml
fiabilite: 🟠 contesté
fiabilite_note: "Auteur année, Revue vol(n°), pages, N=…, d=…, IC 95% […]"
```

**Le verdict seul ne vaut rien.** Sans la référence, c'est un avis ; avec, c'est
une information vérifiable par quelqu'un d'autre — ou par soi-même dans deux ans.

La règle qui va avec : ne jamais écrire « prouvé », « démontré » ou « validé
scientifiquement » sans une référence à côté. Si on ne peut pas vérifier, on écrit
« non vérifié ».

> **À trancher.** Le barème exact. Trois niveaux suffisent — solide, contesté,
> réfuté — mais voir la décision 06, qui en impose un quatrième.

---

## 06. La valeur par défaut, qui décide de tout

Question en apparence anodine : que met-on dans le champ quand on n'a rien vérifié ?

| Option | Conséquence |
|---|---|
| **Laisser vide** | Impossible de distinguer « pas encore vérifié » de « oublié ». Non interrogeable. |
| **Mettre « solide »** | Confortable et faux. Si tout est vert, le vert ne signale plus rien — et les rares notes réfutées se noient. |
| **Valeur explicite « non évalué »** | Dit la vérité, interrogeable, produit une file de travail au lieu d'un faux propre. |

> ⚠️ **Calibrage — le chiffre à connaître avant de s'engager**
>
> Sur un corpus de psychologie, dev perso et séduction issu de livres grand public,
> **un tiers seulement des concepts vérifiés survit intact**. Le reste est soit
> nettement exagéré par rapport à l'étude d'origine, soit réfuté par une réplication.
>
> Et la vérification coûte cher : **entre vingt minutes et une heure par concept** —
> retrouver la source primaire, lire la méta-analyse, noter le chiffre exact et
> l'intervalle de confiance. À ce rythme, trois cents concepts représentent
> plusieurs mois de travail à temps partiel.
>
> **Conséquence pratique :** une approche science-based ne peut pas être un
> préalable à l'écriture, sinon rien ne s'écrit. C'est une *dette assumée et
> visible*, que la valeur par défaut rend mesurable.

> **À trancher.** Est-ce qu'un concept peut entrer sans verdict ? Répondre non est
> plus pur et beaucoup plus lent. Répondre oui impose la valeur par défaut explicite.

---

## 07. Ce qui échappe au verdict

Le champ de fiabilité mesure la solidité empirique d'une *affirmation sur le monde*.
Beaucoup de notes n'en font aucune.

« Que fait telle option de telle commande » n'a pas de base empirique à qualifier :
c'est vrai ou faux, vérifiable en trois secondes. Exiger un verdict et une
source-livre sur ce type de note pousse à inventer une filiation qui n'existe pas —
la source réelle est la documentation officielle.

> ⚠️ **Le principe général, celui qui compte.** Quand une règle produit surtout des
> faux positifs, **c'est la règle qu'il faut corriger, pas les notes**. Un audit qui
> signale trois cents problèmes dont deux cents n'en sont pas devient du bruit, et
> on cesse de le lancer.

> **À trancher.** Quels domaines sont exemptés. Le technique, clairement. Le sport
> est le cas limite : la physiologie de vulgarisation est aussi fragile que la
> psycho, donc probablement pas exempté.

---

# Partie III — L'opérationnel

## 08. La mémorisation intégrée à la note

Chaque note atomique se termine par des cartes de révision, écrites en texte brut
dans la note et synchronisées vers Anki par un plugin.

**Pourquoi ce n'est pas optionnel.** La pratique de récupération et la répétition
espacée sont les deux seules techniques d'apprentissage classées « utilité élevée »
dans la revue de Dunlosky et al. 2013 (*Psychological Science in the Public
Interest* 14(1), 4-58) — contre « utilité faible » pour le surlignage, la relecture
et le résumé. Écrire une note sans en tirer de question, c'est faire du surlignage
sophistiqué.

**Le bénéfice caché.** Formuler une question force à vérifier qu'on a compris.
C'est le meilleur détecteur de note floue qui existe : si aucune question nette
n'en sort, la note ne dit rien de précis.

> ⚠️ **Deux pièges qui coûtent cher**
>
> **Un seul deck à plat.** Mélanger tous les domaines dans une seule pile rend
> certaines questions ambiguës : la même formulation peut avoir deux réponses
> justes selon le domaine. Des sous-decks par domaine dès le départ suppriment le
> problème — le réparer après mille cartes, non.
>
> **Les identifiants écrits à la main.** Le plugin écrit un identifiant dans la
> note après création. En écrire un soi-même produit un échec silencieux : le
> plugin tente de mettre à jour une carte qui n'existe pas, échoue, et n'enregistre
> jamais le fichier. Des cartes peuvent rester bloquées des mois sans aucun signal.

> **À trancher.** Cartes obligatoires dès la création, ou tolérées en dette ? La
> seconde option tient, à condition que l'audit les réclame et qu'on le lance.

---

## 09. Un audit mécanique, lecture seule

Un script qui parcourt le vault et signale ce qui est vérifiable sans jugement :
doublons de nom, liens morts, frontmatter cassé, champs manquants, sections
absentes, restes de template, tags incomplets, notes orphelines.

**La règle de conception.** *Il ne modifie rien.* Il produit un rapport. La
correction est une décision, et une décision ne s'automatise pas — mais le
*constat*, si.

**Ce qu'il faut savoir.** Le script a ses propres angles morts, et ils sont
sournois : une expression régulière trop stricte peut ignorer des dizaines de notes
qui ont pourtant le problème — ou l'inverse. Traiter son compteur comme une vérité
absolue est une erreur ; il faut le vérifier lui aussi, de temps en temps, sur un
échantillon lu à la main.

> **À trancher.** Partager le même script, ou chacun le sien ? Si les conventions
> divergent, un script commun devient vite un nid de faux positifs.

---

## 10. Ne jamais renommer depuis le terminal

Obsidian ne met à jour les liens entrants que lors d'un renommage fait *dans*
Obsidian (F2). Un `mv` depuis le shell casse tous les liens entrants sans aucun
message.

C'est la seule règle qui mérite d'être absolue, parce que la casse est silencieuse
et ne se détecte qu'au prochain audit — potentiellement des semaines plus tard,
quand on ne sait plus ce qui a été renommé.

> **À trancher.** Rien. C'est une contrainte de l'outil, pas un choix de méthode.

---

# Partie IV — Le périmètre

## 11. Le livre n'est pas le savoir

C'est la décision la plus structurante, et celle où deux approches divergent le
plus naturellement.

| Entrée par la note | Entrée par le livre |
|---|---|
| L'idée est l'unité. Le livre est une source qu'on cite. | On part du PDF, on le lit, on en extrait les notes. |
| La fiche de livre reste mince : métadonnées, thèse, analyse perso, actions. | Force une source à chaque idée, garantit la traçabilité. |

Ce ne sont pas deux structures concurrentes : ce sont deux **points d'entrée** dans
la même structure. Les deux aboutissent à des notes atomiques reliées, avec une
fiche de source mince au-dessus.

> ⚠️ **Le risque propre à l'entrée par le livre.** Il n'est pas structurel, il est
> comportemental : le **« collector's fallacy »** — accumuler des livres en croyant
> accumuler du savoir. Le symptôme est mesurable : compter les PDF, compter les
> fiches, compter les fiches qui ont réellement produit des notes atomiques.
> L'écart entre les trois chiffres dit exactement combien de lecture a été convertie.
>
> Le garde-fou : **un livre ne peut pas entrer sans produire au moins une note
> atomique.** Règle simple, vérifiable par script, et qui transforme la bibliothèque
> en file d'attente plutôt qu'en collection.

> **À trancher.** Le point d'entrée peut différer entre vous sans aucun problème.
> Le garde-fou, lui, mérite d'être adopté des deux côtés.

---

## 12. Écrire la liste de ce qui reste dehors

Plus structurant que la liste de ce qui entre, et presque toujours oublié.

Une fiche de livre demande une thèse et des actions. Cela n'a aucun sens pour de la
fiction de loisir, un cahier d'exercices, un manuel de cours ou une bibliothèque de
jeu. Et un livre **explicitement écarté** après examen ne se fiche pas non plus —
le ficher contredirait la décision de l'écarter.

Sans cette liste, l'audit se remplit de « problèmes » qui n'en sont pas, et on finit
par l'ignorer — ce qui le rend inutile au moment où il signale un vrai problème.

> **À trancher.** Chacun la sienne, écrite le premier jour, dans le fichier de
> conventions. C'est la décision la plus rentable du lot.

---

# Partie V — Où vos deux approches peuvent diverger

*La vraie question n'est pas « qui a raison », mais : qu'est-ce qui doit être
identique pour que vous puissiez vous relire, et qu'est-ce qui peut différer
librement ?*

## Ce qui peut différer sans conséquence

| Divergence | Pourquoi ça ne casse rien |
|---|---|
| Point d'entrée — note d'abord ou livre d'abord | Aboutit à la même structure. Ce n'est qu'un ordre de travail. |
| Arborescence des dossiers | Les liens sont par nom de note, pas par chemin. |
| Granularité effective des notes | Tant que le *critère* est le même (décision 01). |
| Langue des notes | Affaire de confort de lecture. |
| Domaines couverts | Le sport, le style, les langues s'ajoutent indépendamment. |
| Outils de révision et scripts | Chacun le sien, du moment que la syntaxe des cartes est stable chez lui. |

## Ce qui doit être identique pour pouvoir échanger

| Convention | Ce qui casse sinon |
|---|---|
| **Le préfixe de type et le séparateur** | Une note copiée arrive hors convention, et les scripts de l'autre ne la voient pas. |
| **La taxonomie de tags** | Un `soft/psycho` contre un `psychologie` rend toute requête croisée impossible. |
| **Le nom des champs de frontmatter** | `source` / `fiabilite` / `fiabilite_note` — un champ nommé autrement est invisible aux requêtes de l'autre. |
| **Le barème de fiabilité** | Un 🟠 qui ne veut pas dire la même chose des deux côtés rend les verdicts inéchangeables — et c'est la partie la plus coûteuse à produire. |
| **La syntaxe des cartes de révision** | Un séparateur différent, et aucune carte ne passe d'un vault à l'autre. |
| **Le critère de granularité** | Si l'un écrit des notes trois fois plus grosses, aucune citation croisée précise n'est possible. |

> **Le vrai bénéfice d'aligner ces six-là.** Une vérification épistémique coûte
> entre vingt minutes et une heure. Si vos barèmes, vos tags et vos noms de champs
> correspondent, **chaque concept vérifié par l'un est réutilisable par l'autre tel
> quel** — verdict, référence, chiffre. C'est la seule partie du travail qui se
> partage vraiment, et de loin la plus chère à produire.
>
> Sur des domaines partagés — psychologie, séduction, dev perso, stratégie — c'est
> potentiellement des dizaines d'heures économisées de chaque côté.

---

## L'ordre dans lequel décider

Toutes ces décisions ne coûtent pas la même chose à changer plus tard. Par ordre de
coût de revirement, décroissant :

**Irréversibles en pratique — à figer avant la première note**
* Préfixes et séparateur (02)
* Taxonomie de tags (03)
* Noms des champs de frontmatter (05)
* Syntaxe des cartes de révision (08)

**Coûteuses mais faisables — un chantier de quelques heures à cent notes, de plusieurs jours à mille**
* Barème de fiabilité (05-06)
* Critère de granularité (01)
* Découpage des decks (08)

**Modifiables à tout moment**
* Arborescence, domaines couverts, exemptions (07), périmètre (11-12), point d'entrée (11)

> **La seule vraie urgence : trancher les quatre premières ensemble, maintenant.**
> Le reste se discute au fil de l'eau.

---

### 🔗 Connexions
* [[Guide-Anki]] — *le pipeline de synchronisation en pratique.*
* [[Concept-Zettelkasten]] — *le principe d'origine.*
* [[Concept-Active_Recall]] · [[Concept-Répétition_Espacée]] — *les deux techniques qui justifient la décision 08.*
* [[Source-How_to_Take_Smart_Notes]] — *la méthode dont tout ceci descend.*
