---
tags: [meta/guide]
---
# 🧭 Reprise — où en est ce vault

> **À lire en premier quand on reprend le travail dans une nouvelle session.**
> Cette note existe parce qu'une partie de ce qui a été appris n'est écrite **nulle part
> ailleurs** : les régularités constatées d'un livre à l'autre, les pièges techniques
> rencontrés, et les décisions prises en cours de route.
>
> État au **2026-09-28**. Construit en une session, à partir d'un vault vide.

---

## 1 · Ce qu'il faut lire, dans cet ordre

| Fichier | Ce qu'il contient |
|---|---|
| [[Guide-Conventions]] | **la constitution.** Les 12 décisions tranchées, plus l'arborescence, la langue et les plugins. Tout le reste en découle |
| [[Guide-Méthode_Zettelkasten]] | le document d'origine, apporté par Yinpi — le raisonnement derrière chaque décision |
| cette note | l'état, les constats, les pièges |
| [[Guide-Stratégie_Lecture]] | comment les trois listes de lecture s'articulent, et le filtre ⏳ |
| [[Ref-Lecture_Lacunes]] | les six axes absents de la bibliothèque — la seule file de lecture qui reste |
| [[Guide-Anki_Workflow]] | la synchronisation des cartes, et ses trois pièges |
| [[MOC-Audit]] | le tableau de bord Dataview · et `python3 Scripts/audit.py` pour le reste |

**Les quatre index par domaine :** [[MOC-Esprit]] · [[MOC-Social]] · [[MOC-Tech]] · [[MOC-Corps]].

---

## 2 · L'état, en chiffres

*Recalculé depuis les fichiers le 2026-10-02. **Ne pas faire confiance à ce bloc sans le
revérifier** — il a été périmé deux fois, et c'est le seul endroit du vault qu'aucun
contrôle ne vérifie.*

```
233 notes · 163 Concept- · 41 Source- · 19 Ref- · 5 MOC- · 5 Guide-
0 erreur · 0 alerte · 0 info — l'audit est entièrement vide
466 cartes écrites · 407 dans Anki, **59 neuves à scanner**
87 titres à l'inventaire, 60 sur le disque (394 Mo) — dont 1 EPUB
```

| Domaine | `Concept-` | `Source-` | `Ref-` |
|---|---|---|---|
| `Esprit/` | 84 | 23 | 6 |
| `Social/` | **61** | 14 | 7 |
| `Corps/` | **14** | 2 | 1 |
| `Tech/` | **4** — toutes `⬜` | 2 | 0 |
| `Langues/` | **0** | 0 | 0 |

**Verdicts :** 🟠 68 · ⬜ 66 · 🟢 20 · 🔴 5 · 🔵 4 · **⚪ 0**
Les **97 verdicts datés** portent une `fiabilite_date` ; horizon 24 mois, le plus ancien a
0 mois. **La file de vérification est vide** — les 42 dettes de la construction ont toutes
été examinées, les 4 restantes sont en `🔵 invérifiable`.

**Inventaire :** 34 fichés · 13 lu-sans-fiche · 19 illustration · 21 dehors.
**12 titres du disque ne sont sur aucune liste de lecture** — niveau tranché, conservation
tranchée. **Aucun livre `fiché` n'est sans fiche.** *Style* et *Exercised* ont été acquis et
convertis le même jour, le 2026-10-02 — les deux dettes ont vécu quelques heures.

**Révision Anki : 27 cartes vues sur 466.** C'est la seule boucle de rétroaction qui trouve
ce que ni l'audit ni Claude ne trouvent — elle a détecté les 92 questions sans contexte et
trois énoncés incompréhensibles. **Marquer d'un drapeau toute carte qu'on ne comprend pas**,
et en reparler à cinq ou six.

---

## 3 · Ce qui a été fait

**La liste 1 compte 41 titres**, en cinq phases : Moteur, Véhicule, Navigation,
Stratégie, Socle. Elle en comptait 34 à la construction ; **quatre sont entrés le
2026-09-29** — *Attached* (phase 3), les deux Goffman et la *Critique de la raison
pure* (phase 5) — **puis *Make It Stick* le 2026-10-02**, et **tous les cinq sont
convertis depuis**. Plus **7 romans** au niveau `illustration` : les quatre dystopies
du contrôle, deux tomes de *Fondation*, *I, Robot*.

**Il ne reste aucun livre à lire**, et aucune file de travail. Les deux derniers
titres — *Style* (Williams & Bizup, tête de phase 2) et *Exercised* (Lieberman,
phase 1) — ont été acquis et convertis le 2026-10-02, et ils n'entraient pas comme
les trente-neuf autres : ce sont les **deux premiers venus de
[[Ref-Lecture_Lacunes]]**, donc d'un **axe constaté absent** plutôt que d'une liste
d'envies. Ils ont produit **20 notes et 59 cartes**, les deux convertis en entier — douze
leçons pour *Style*, treize chapitres pour *Exercised*. *Style* est devenu **le
livre le plus productif du vault** avec 11 notes atomiques, devant les trois Greene ;
*Exercised* en a 9.

**Ce qu'ils ont changé de plus que leur contenu :**

| | |
|---|---|
| `corps/` **a presque triplé** | 5 → 14 notes, et c'est le domaine au meilleur ratio de `🟢` après `esprit/` |
| `social/` a reçu **le régime `⬜` de `tech/`** | onze règles de conception de la prose, évaluées par contre-exemple. Première application de la décision 07 hors de `tech/` — et `⬜` est devenu le verdict **majoritaire** du vault, 66 sur 158 |
| le contrôle d'atomicité **a servi** | les 10 premières notes sont tombées dans le dernier décile, et la relecture a trouvé **une vraie couture** : `Concept-Topique_Et_Emphase` portait aussi la distinction cohésion/cohérence, détachée en [[Concept-Cohésion_Et_Cohérence]]. Les 10 suivantes ont été écrites sous le seuil — le contrôle a changé la façon d'écrire, pas seulement trié |
| **la règle d'autonomie aussi** | une carte demandait *« quel procédé cette note nomme-t-elle »*, sans référent en révision. Troisième contrôle du vault à trouver quelque chose qu'aucune relecture humaine n'avait vu |
| **une contradiction entre deux sources** | [[Concept-Norme_Des_Huit_Heures]] (Lieberman) contre [[Source-Why_We_Sleep]] (Walker) sur la dose de sommeil. C'est la **première** du vault, et elle est inscrite en `## Actions` plutôt que lissée |
| une question de gouvernance **est ouverte** | onze notes sur l'écriture justifient `social/écriture` au sens de la règle des 5 — mais le seuil était connu de celui qui les écrivait. L'argument tient moins bien à onze qu'à cinq, sans tomber. Voir le bas de [[MOC-Social]] |
| la structure de *Style* **n'est pas celle de son titre** | ce n'est pas « clarté puis grâce » mais une **montée d'échelle** : phrase, passage, section, document, puis ce que la forme engage. Les notes les plus citables hors écriture sont les plus hautes dans cette échelle |

> **Le pli à prendre :** un livre qui vient d'une lacune apporte sa justification avec
> lui — la preuve de l'absence est déjà écrite, datée, et vérifiable. C'est l'inverse
> des six niveaux posés par défaut qu'il a fallu relire en bloc le 2026-10-01.

### Ce qui a changé par rapport au guide d'origine

Quatre ajouts au modèle, tous décidés en cours de route et consignés dans les conventions :

| Ajout | Pourquoi |
|---|---|
| **5ᵉ valeur au barème : `⬜ non applicable`** | 43 notes n'affirment rien d'empirique — définitions, préceptes, formalismes. Sans cette valeur elles seraient coincées en `⚪` et pollueraient la file de dettes |
| **4ᵉ niveau de périmètre : `illustration`** | la fiction lue pour sa structure n'est ni un manuel ni du loisir. **Règle associée : une fiction ne crée jamais de `Concept-`** — elle est citée comme exemple depuis une note existante |
| **Règle des 3 cartes** (décision 01) | le signal de découpe est mécanisable par `grep -c '^Q:'`, donc gratuit |
| **`corps/`** | né à la règle des 5, sans qu'on ait eu à décider. Premier test réel de cette règle |
| **Règle d'autonomie des cartes** (décision 08) | ajoutée le 2026-09-28 après usage réel : 92 cartes sur 350 étaient irrésolubles en révision. Une question doit nommer son sujet ; préfixe `**Titre** — ` là où elle ne se suffit pas |
| **Signal d'atomicité** (décision 01) | 2026-09-30 : le signal d'origine ne pouvait pas se déclencher. Le nouveau mesure la section `## L'idée` seule — une longue vérification est un bon signe, une longue idée non — et se présente comme un échantillon, jamais comme un verdict |
| **`fiabilite_date`** (décision 05) | 2026-09-30 : un verdict empirique dépend d'un état de la littérature, et cet état a une date. Obligatoire sur `🟢🟠🔴`, absent de `⚪⬜` — une définition ne vieillit pas. Horizon **24 mois**, au-delà l'audit rouvre la dette. **Le seul contrôle du vault dont le déclenchement ne dépende de la discipline de personne** |
| **6ᵉ valeur au barème : `🔵 invérifiable`** (décision 05) | 2026-10-02, après que le trou s'est présenté **quatre fois**. `⚪` disait deux choses incompatibles — « pas encore examiné » et « examiné, rien ne permet de trancher ». La seconde restait dans la file, où quelqu'un refaisait un travail déjà fait. **`🔵` porte une date et se périme** comme un verdict tranché : une littérature peut paraître. C'est ce qui le sépare de `⬜`, qui ne vieillit pas |
| **Inventaire unique des livres** | 2026-09-29 : `Ref-Périmètre_Bibliothèque` est devenu [[Ref-Bibliothèque]], l'inventaire complet — 84 titres, possédés ou non, avec niveau, domaine et liste d'origine. Les `Ref-Lecture_*` ont perdu leurs colonnes Domaine et Périmètre : un niveau n'est déclaré qu'à un endroit |

---

## 4 · Les cinq constats qui n'existent nulle part ailleurs

C'est la partie de cette note qui ne peut pas être reconstituée à partir du vault.

### 4.1 · Garder le geste, jeter le mécanisme — **cinq fois**

Le mode de défaillance dominant de ce corpus. Une pratique utile arrive accompagnée d'une
explication fausse, et la pratique survit à la réfutation de l'explication.

| Mécanisme réfuté ou contesté | Ce qui survit |
|---|---|
| [[Concept-Volonté_Comme_Ressource]] 🔴 — *ego depletion* | réduire le nombre de décisions reste utile |
| [[Concept-Posture_De_Pouvoir]] 🔴 — effets hormonaux | être physiquement à l'aise change ce qu'on fait de son attention |
| [[Concept-Cerveau_Triunique]] 🔴 — modèle de MacLean | certaines réactions corporelles sont peu contrôlables |
| [[Concept-Ombre_Et_Traits_Refoulés]] 🟠 — appareil jungien | une réaction disproportionnée mérite un examen |
| [[Concept-EMDR_Mécanisme_Et_Effet]] 🟠 — mouvements oculaires | la thérapie fonctionne, par exposition |

**Conséquence de méthode :** devant toute prescription appuyée sur un mécanisme, vérifier les
deux séparément. L'une peut tenir sans l'autre.

### 4.2 · L'ego depletion a contaminé **trois** livres de la liste

Ahrens, Newport et Kahneman s'y appuient. Clear la contourne, et c'est pourquoi sa
prescription survit mieux. **Un prix Nobel écrivant sur la fragilité du jugement a repris sans
réserve une littérature qui n'a pas tenu** — ce n'est pas une faute individuelle, c'est la
norme de l'époque, et c'est la meilleure justification du champ `fiabilite`.

### 4.3 · Le taux de survie a suivi exactement le calibrage annoncé

Le guide d'origine annonçait « un tiers seulement des concepts vérifiés survit intact ».

| Après la phase | Notes intactes / évaluées |
|---|---|
| 1 — Moteur | 47 % |
| 2 — Véhicule | 37 % |
| 3 — Navigation | 31 % |
| 4 — Stratégie | 27 % |
| 5 — Socle | **38 %** |

La remontée finale n'est pas un hasard : la phase 5 repose sur des **théorèmes** et de
l'épidémiologie, pas sur de la psychologie sociale de laboratoire. Et `social/` n'a
**qu'une seule note 🟢 sur 38**, contre 3 `🔴` sur les 5 du vault.

### 4.4 · Une seule critique, appliquée six fois

[[Concept-Preuve_Silencieuse]] est le défaut structurel de **six livres** : les portraits de
Newport, les cas de Voss, les anecdotes de Greene ×2, les réussites de Manson, le témoignage
de Frankl. J'ai écrit la même remarque six fois avant que la note existe — il a fallu attendre
le 23ᵉ livre. **C'est exactement ce qu'un Zettelkasten est censé produire, et ça montre aussi
sa lenteur.**

### 4.5 · Les meilleures notes ne viennent pas des livres les plus récents

Les 16 notes tirées des cinq textes primaires — Sun Tzu, Machiavel, Clausewitz, Marc Aurèle,
Nietzsche — sont presque toutes `⬜`, et **les plus citées du vault**. Elles sont abstraites,
donc portables. Symétriquement, les meilleures notes techniques ne parlent pas de code :
[[Concept-Orthogonalité]] justifie la décision 03, [[Concept-DRY]] la source unique du
périmètre, [[Concept-Fenêtre_Brisée]] l'existence de l'audit.

---

## 5 · Les pièges techniques rencontrés, et leurs corrections

| Piège | Ce qui s'est passé | Correction |
|---|---|---|
| **Le plugin écrase sa config** | l'ajout de `Corps` à `FOLDER_DECKS`, fait sur le disque pendant qu'Obsidian tournait, a disparu au scan suivant | **toujours passer par le panneau de réglages du plugin.** Contrôle ajouté à l'audit ; documenté dans [[Guide-Anki_Workflow]] |
| **Un scan sans couche de texte** | `The_48_Laws_of_Power.pdf` n'avait aucun texte extractible | océrisé, 476 pages, qualité mesurée à **0,060 %** d'anomalies. Nécessite `tesseract-data-eng` |
| **Un niveau absent du script** | `illustration` ajouté au modèle mais pas à la liste reconnue par `audit.py` — il ignorait silencieusement ces lignes | corrigé. **C'est l'angle mort annoncé par la décision 09 : vérifier le script lui aussi** |
| **Un filigrane injecté** | `Why_We_Sleep.pdf` porte une URL **381 fois**, une par page, au milieu du texte | filtrer à l'extraction, sinon il entre dans les citations |
| **Un lien de catégorie impossible** | j'ai écrit `[[Source-Beyond_Good_and_Evil]]` pour un livre `lu-sans-fiche`, qui n'aura jamais de fiche | l'audit l'a détecté. Les notes de ces livres pointent le **PDF** |
| **Noms de fichiers non conformes** | 12 PDF arrivés avec espaces, tirets, casse basse, slugs d'URL | renommés. **Déplacer un PDF ne casse rien, le renommer casse la fiche qui le cite** |
| **Cartes écrites la note sous les yeux** | 92 questions sur 350 renvoyaient à « ce principe », « cette règle », « le livre » — lisibles à l'écriture, illisibles en révision, où Anki tire dans le désordre | préfixe `**Titre** — `, règle inscrite en décision 08, contrôle ajouté à l'audit. **Le défaut est invisible au rédacteur par construction** : c'est le seul du lot qu'aucune relecture de la note ne révèle |
| **Une duplication qui avait commencé à divarier** | le domaine et le niveau de chaque livre vivaient dans deux fichiers. Pas encore de divergence sur les niveaux, mais déjà sur les noms : *De la guerre* dans la liste, `On_War` au périmètre — donc irréconciliable par script | inventaire unique, et les listes n'en parlent plus. **Le signal d'alarme n'était pas une erreur mais un nom qui ne s'apparie pas** |
| **Un garde-fou borgne** | le garde-fou 11 vérifiait qu'une fiche produit une note, jamais qu'un livre fiché a une fiche. **Huit livres attendaient en silence**, six depuis la construction du vault | contrôle ajouté, comptés en dette. Un garde-fou qui ne teste qu'un sens laisse passer l'autre |
| **Un instrument mort qui avait l'air vivant** | la règle des 3 cartes devait signaler les notes non atomiques : `grep -c '^Q:' > 3`. Mesure sur 137 notes — **118 en ont exactement 3, 19 en ont 2, aucune n'en a 4**. Le nombre de cartes est un choix du rédacteur, pas une propriété de la note : la règle mesurait sa propre observance | remplacée par la longueur de prose de la seule section `## L'idée`, au 9ᵉ décile, et **présentée comme un échantillon de relecture, pas comme un verdict**. Vérifiée dans les deux sens le jour même : une note gardée, une scindée |
| **Déplacer une carte entre deux notes** | trois échecs en cascade avant même d'arriver au précédent : le plugin ne supprime pas l'ancienne carte → la nouvelle est refusée comme doublon → l'empreinte du fichier est enregistrée malgré l'échec, donc jamais retentée | **ne jamais déplacer une carte.** Supprimer d'un côté, scanner, supprimer l'orpheline, puis écrire dans la cible une carte **neuve, formulée autrement** — un énoncé neuf ne peut pas être un doublon. **`orphelines.py` compare les ensembles, pas le placement** : il ne voit pas le piège suivant, d'où le contrôle d'alignement de [[Guide-Anki_Workflow]] |
| **🔴 Un trou dans la suite des identifiants** | **le plugin apparie les identifiants aux cartes par ordre d'apparition, pas par adjacence** : le n-ième id va à la n-ième carte, où que le commentaire soit écrit. Une carte sans id placée ailleurs qu'en dernier **vole l'identifiant de la suivante**, et le scan écrase la note Anki voisine avec le mauvais contenu. Vérifié le 2026-10-02 sur deux notes | **une carte sans identifiant doit toujours être la dernière de son bloc** — donc on ajoute une carte **à la fin, jamais au milieu**. Réparation : tasser les identifiants en tête. **Contrôle ajouté à `audit.py`, hors réseau et en erreur** — un trou est signalé avant qu'un scan puisse faire le dégât. ⚠️ ma première tentative de réparation a échoué pour avoir cru à une insertion « un cran trop bas » |
| **Une question sans critère de réussite** | « quelle nuance escamote-t-il ? » admet dix réponses défendables : impossible de savoir si la sienne compte. **Trouvé par Yinpi en révision, sur trois cartes** — ni l'audit ni Claude ne pouvaient le voir | nommer les candidats dans la question, le plus souvent un choix binaire. Contrôle ajouté en **info**, exemption par `cartes_relues:`. ⚠️ écrit deux fois : le motif `quelle?` ne couvrait pas « quel », donc il laissait passer la moitié des cas — **8 % du corpus antérieur**, pas 4 % |
| **Le tableau de bord était aveugle à un domaine entier** | les 5 requêtes Dataview de [[MOC-Audit]] listaient `Esprit Social Tech Langues` et **pas `Corps`**, né après leur rédaction. Cinq notes, dont trois verdicts `🟢`, invisibles depuis la création du domaine | `Corps` réintégré aux cinq, et **contrôle ajouté** : l'audit compare les `FROM` aux dossiers réels. Même angle mort que `FOLDER_DECKS` côté Anki, et il a fallu le chercher pour le voir |
| **Une dette qui n'était pas du travail** | 6 livres étaient `fiché` — le niveau le plus lourd — sans fiche, alors que [[Ref-Lecture_Ordre_de_Priorité]] les jugeait « doublons » ou « candidats `🔴`/`🟠` » **depuis le premier jour**. Le niveau avait été posé par défaut et jamais relu contre le jugement porté ailleurs | reclassés le 2026-10-01 : 3 en `dehors`, 3 en `lu-sans-fiche`. **Une dette n'est pas toujours du travail à faire, c'est parfois un classement à corriger** — et l'audit ne peut pas distinguer les deux : il voit qu'une fiche manque, pas qu'elle n'aurait jamais dû être attendue |
| **Une file qui ne pouvait pas se vider** | le signal d'atomicité a un seuil **relatif** — le 9ᵉ décile — donc il renvoie toujours un dixième des notes. Une séance de relecture ne laissait aucune trace, et la suivante aurait relu les mêmes | champ `atomicite_relue`, même motif que `fiabilite_date`. L'audit ne signale qu'une note du décile qui ne le porte pas. **Une file infinie vaut une règle muette** |
| **Les index dérivent de ce qu'ils décrivent** | trouvé **trois fois à la main** : compteurs périmés, `Corps/` absent des 5 requêtes Dataview, et **8 notes jamais listées dans `MOC-Social`** — dont `Règle_7_38_55`, une des 5 seules `🔴` du vault, et une section `Négociation` entière | contrôle ajouté : l'audit compare chaque `Concept-` à son index. Omission = alerte, verdict faux = **erreur**. **C'est la seule classe de défaut qui s'est répétée** — tout artefact tenu à la main dérive |

---

## 6 · Ce qui reste à faire

### ✅ Le trou du barème est bouché — `🔵 invérifiable`, 2026-10-02

`⚪` disait deux choses incompatibles : « pas encore examiné » et « examiné, et rien ne
permet de trancher ». La seconde restait dans la file de dette, où elle aurait été
réexaminée indéfiniment. Le trou s'est présenté **quatre fois** avant d'être traité, et
une fois j'ai contourné en reclassant en `⬜` ([[Concept-Rareté_Comme_Valeur]]) — un
contournement que j'avais signalé comme tel.

Les trois valeurs voisines se distinguent maintenant par **ce qu'on a fait et ce qui
existe** : `⚪` on n'a pas cherché · `🔵` on a cherché, rien n'existe · `⬜` il n'y avait
rien à chercher. Détail en décision 05.

### ✅ La file de vérification est vidée — 2026-10-02

**Les 42 dettes de départ ont toutes été examinées.** Il en reste quatre, et elles ne
sont pas en attente d'examen : elles ont été examinées et **rien ne permet de les
trancher**. Chacune porte dans son `fiabilite_note` ce qu'il faudrait pour le faire.

| Dette restante | Ce qu'il faudrait |
|---|---|
| `Structure_Ascendante` | comparer deux protocoles de prise de notes sur une production ultérieure |
| `Réserve_De_Matière` | comparer deux modes de préparation sur une mesure d'anxiété et de fluidité |
| `Paradoxe_Du_Succès` | une cohorte suivie avant et après un succès, avec le flux de sollicitations accepté |
| `Apparences_Normales` | mesurer la détection d'une non-exécution de civilité contre celle d'un acte saillant |

**Le résultat dominant, sur 38 notes vérifiées : 36 fois l'appui existait et l'auteur ne
le citait pas.** Ce n'est pas que ces livres inventent — c'est qu'ils ne cherchent pas.
Et quatre fois, la littérature a fait mieux que confirmer :

* elle a **validé un critère que la note avait inventé** — [[Concept-Terrain_De_Mort]], les
  dispositifs d'engagement agissent précisément sur les problèmes d'exécution
* elle a **confirmé un doute** qu'une note exprimait contre son propre auteur —
  [[Concept-Levier_Des_Minorités_Organisées]], Watts & Dodds contre le modèle de Bernays
* elle a montré que **le vocabulaire d'un auteur désignait la branche qui ne marche pas** —
  [[Concept-Empathie_Tactique]], où « empathie tactique » est en fait de la prise de
  perspective, seule branche efficace chez Galinsky et al.
* elle a donné **un nom et une réplication** à un procédé présenté comme une trouvaille —
  [[Concept-Audit_D_Accusation]], c'est le *stealing thunder*

**Et trois fois, c'est moi qui avais tort :** surgénéralisation sur
[[Concept-Menace_Sur_L_Image_De_Soi]], surcorrection *dans le sens modeste* sur
[[Concept-Rejet_Comme_Filtre]], et un mécanisme inventé de toutes pièces sur la
réparation des identifiants Anki.

À 20 min – 1 h par concept, c'est **12 à 37 heures**. À payer **par ordre d'utilité**, jamais
d'arrivée : le premier tableau de [[MOC-Audit]] les trie par nombre de liens entrants.

Les plus rentables sont celles qui servent de prémisse à d'autres —
[[Concept-Dépendance_Au_Regard]], [[Concept-Polarisation]],
[[Concept-Vulnérabilité_Comme_Signal]] portent chacune trois notes de séduction.

**19 des 37 sont dans `social/`**, le domaine le plus fragile : coût le plus élevé, rendement
attendu le plus faible.

### Trous connus

- **`Langues/` est vide.** `English_Phrasal_Verbs` est `lu-sans-fiche`, et la décision 02b a
  écarté un préfixe `Vocab-`. ⚠️ **À rouvrir avant d'attaquer le vocabulaire :** l'ancien vault
  avait un type de note Anki `Vocabulaire_Elite` avec un champ *Exemple*, conservé dans la
  configuration du plugin et inutilisé.
- **Une note manquante que rien ne peut combler par la fiction :** la **spécification
  incomplète**, qu'illustre parfaitement *I, Robot* — mais une fiction ne crée pas de
  `Concept-`. Elle devra venir de littérature technique. Voir [[Source-I_Robot]].
- **[[Ref-Lecture_SciFi_Stratégique]]** : **12 romans sur 18 pas encore acquis.**
  L'ordre d'acquisition suit désormais une règle — d'abord celui dont la note cible
  existe déjà. *The Traitor Baru Cormorant* est le seul apparié qui manque.
- ✅ **Les quatre déplacements de lecture sont appliqués** — les deux derniers le
  2026-10-02 : *Thinking, Fast and Slow* de la phase 5 à la **phase 1**, *Thinking in
  Systems* de la phase 1 à la **phase 4**. Sans effet rétroactif, les 39 titres étant
  lus : la liste dit désormais ce qu'il **aurait fallu** faire. Il reste deux dépendances
  inter-phases que le déplacement ne résout pas — *Why We Sleep* et *The Body Keeps the
  Score* sont au Socle à juste titre, mais lus trop tard pour ce qu'ils conditionnent.

### Une contradiction assumée, à ne pas « corriger »

[[Concept-Terrain_De_Mort]] dit de supprimer ses options ; [[Concept-Surface_D_Exposition]] et
[[Concept-Optionalité]] disent de les garder. **Le critère de partage est écrit dans la
première note** — supprimer si le problème est l'exécution, garder si c'est l'information.
C'est la seule contradiction explicite du vault, et elle est plus informative que si elle
avait été tranchée.

---

## 7 · Réflexes à conserver

1. **Lancer `python3 Scripts/audit.py` avant et après chaque séance.** Il ne modifie rien.
2. **Jamais de `mv` ni de `rm` sur un `.md`** — F2 ou glisser-déposer dans Obsidian, décision 10.
3. **Ne jamais écrire un identifiant de carte à la main.** Échec silencieux garanti.
   Et **lancer `python3 Scripts/orphelines.py` après tout scan qui a retiré ou déplacé
   une carte** : le plugin ne supprime pas, il laisse des orphelines sans le dire.
4. **Vérifier dans le PDF avant d'écrire.** Sur 36 livres, six étaient en traduction sans que
   rien ne l'annonce, un était un scan, un portait un filigrane, et *Propaganda* s'est révélé
   français alors que je le cherchais en anglais.
5. **Une fiction ne crée jamais de `Concept-`.**
6. **Quand une règle produit surtout des faux positifs, corriger la règle** — pas les notes.

### 🔗 Connexions
* [[Guide-Conventions]] — *les 12 décisions, et tout ce qui en découle.*
* [[Guide-Méthode_Zettelkasten]] — *le raisonnement d'origine.*
* [[MOC-Audit]] — *l'état réel, en direct.*
