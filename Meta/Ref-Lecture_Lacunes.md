---
tags: [meta/ref]
---
# 🕳️ Lacunes — les axes que la bibliothèque ne couvre pas

> **Référence stable : la liste des sujets absents, et la preuve de leur absence.**
> Les trois `Ref-Lecture_*` disent quoi lire et dans quel ordre. Celle-ci dit
> **ce qui n'est sur aucune des trois** — et pourquoi on le sait.
>
> État au **2026-10-02**, établi quand les 39 titres de
> [[Ref-Lecture_Ordre_de_Priorité]] étaient tous convertis et qu'aucune liste de
> lecture n'avait plus de file. C'est le moment où la question se pose : une
> bibliothèque sans file n'est pas une bibliothèque complète, c'est une
> bibliothèque dont on ne connaît plus les bords.

**Cette note ne déclare ni niveau de périmètre ni domaine.** Un titre candidat n'a
pas encore de traitement — il en reçoit un dans [[Ref-Bibliothèque]] **le jour où il
est acquis**, et pas avant. Les porter ici les ferait divarier comme les
`Ref-Lecture_*` avaient commencé à le faire.

| | |
|---|---|
| lacunes retenues | **6** |
| titres candidats | **11** |
| dont *Lindy* ⏳ | **4** — Popper, Thucydide, Plutarque, Brooks |
| lacunes fermées | **2** — les n° 3 et 4, le 2026-10-02 |
| notes produites par les deux | **20** · 59 cartes |

---

## Comment une lacune a été établie

C'est la partie de cette note qui ne se reconstitue pas depuis le vault : **trois
tests, et un sujet n'entre ici que s'il en passe au moins un.** Sans ça, « il
manque des livres » est une opinion sans fin — on peut toujours en nommer un.

| | Test | Ce qu'il attrape |
|---|---|---|
| **1** | **Le vocabulaire sans source.** Un terme que les notes emploient pour juger, mais qu'aucun livre de l'inventaire n'enseigne. Mesuré par `grep` | la lacune **n° 1** — et elle ne pouvait être trouvée que comme ça |
| **2** | **La phase contre son propre énoncé.** Chaque phase de la liste 1 déclare *ce qu'elle achète*. On compare à ce qu'elle contient | les lacunes **n° 3, 4, 5** |
| **3** | **La place occupée.** Combien de titres pour un sous-domaine, zéro pour un autre. Le rayonnage est une déclaration de priorité, qu'on l'ait voulu ou non | les lacunes **n° 2, 6** et les deux remarques de proportion |

**Ce que les trois tests ont en commun :** ils se mesurent **sur le vault**, pas sur
une idée de ce qu'une bibliothèque devrait contenir. Un sujet qui ne passe aucun des
trois n'est pas une lacune — c'est un livre que quelqu'un a envie de recommander.

> ⚠️ **Le test 1 est le seul qui ne dépende de la discipline de personne**, comme
> `fiabilite_date` parmi les contrôles d'audit. Les tests 2 et 3 demandent un
> jugement ; celui-là se relance avec un `grep` et répond seul.

---

## Les six lacunes, par gravité

| # | Lacune | La preuve, prise dans le vault | Statut |
|---|---|---|---|
| **1** | **Méthodologie de la preuve** | `grep -rni "popper"` → **0**. `grep -rli "méta-analyse\|taille d'effet\|réplicat"` → **57 fichiers** | ouverte |
| **2** | **Argent et institutions** | **1 note** sur l'argent — [[Concept-Loi_De_Viabilité_Financière]], et elle vient de Newport en passant | ouverte |
| **3** | **L'écriture** | phase 2, 4 titres, **4 oraux ou interpersonnels** | **fermée** — 2026-10-02 |
| **4** | **Le corps au-delà du sommeil** | `Corps/` = **5 notes, 1 fiche** — et c'est [[Source-Why_We_Sleep]], le plus critiqué de la liste | **fermée** — 2026-10-02 |
| **5** | **L'histoire** | **0 titre**, alors que la phase 4 est bâtie sur l'anecdote historique et le dit : *« zéro donnée »* | ouverte |
| **6** | **`tech/`** | **4 notes, toutes `⬜`, 1 fiche** — un domaine déclaré et quasi vide | **à trancher**, voir plus bas |

---

## 1 · L'instrument empirique n'est pas dans la bibliothèque

**C'est la lacune qui se démontre toute seule.**

```
grep -rni "popper"                                          → 0 occurrence
grep -rli "méta-analyse|taille d'effet|réplicat|p-hacking"  → 57 fichiers
```

Tout l'appareil `fiabilite` (décision 05) est un **critère de falsifiabilité
appliqué**, et aucun livre de l'inventaire ne l'enseigne. Les sept verdicts fragiles
de la liste 1 citent Sisk 2018, Maier 2022, Macnamara 2014, Guzey 2019 — c'est-à-dire
la littérature de la crise de la réplication, **utilisée comme outil sans avoir été
lue comme sujet**.

Le Socle contient la *philosophie* de la connaissance : Kant pour les limites du
savoir, Nietzsche pour l'origine des valeurs, Taleb pour les queues et
[[Concept-Preuve_Silencieuse]]. Il ne contient pas la *méthode* de l'évidence.

**Et par la règle de [[Guide-Stratégie_Lecture]] — « les instruments d'abord, hors
phase » — c'est exactement le type de livre qui ne devrait pas pouvoir manquer.**
La règle a été écrite après avoir constaté que le Socle arrivait trop tard. Elle
n'avait pas encore servi à constater qu'il était **incomplet**.

| Candidat | ⏳ | Ce qu'il apporte que ses voisins n'apportent pas |
|---|---|---|
| **Popper — *Conjectures and Refutations*** (1963) | ⏳ | le chapitre 1 **est** le critère que le champ `fiabilite` applique tous les jours. Primaire, et Lindy — même raison que Goffman et Marc Aurèle |
| **Ritchie — *Science Fictions*** (2020) | | la crise de la réplication par un psychométricien : fraude, biais, négligence, battage. Le mode d'emploi des quatre papiers déjà cités dans les notes |
| **Pearl — *The Book of Why*** (2018) | | la liste 1 reproche à Walker des *« affirmations causales surjouées »* — le vault n'a aucun outil d'inférence causale, seulement « corrélation ≠ causalité » comme sagesse populaire |

> **Le plus urgent des seize.** Il manque **sous** le vault, pas à côté : c'est le
> seul candidat dont l'absence affecte la fiabilité de tout ce qui est déjà écrit.

## 2 · L'argent et les institutions — zéro titre

La bibliothèque couvre **soi** (phase 1), **l'interaction** (phases 2-3), et **le
pouvoir comme manœuvre ou comme guerre** (phase 4). Elle ne couvre nulle part les
systèmes dans lesquels tout cela se joue : marchés, entreprises, droit,
bureaucratie, État, capital.

Une seule note porte sur l'argent, et c'est un corollaire :
[[Concept-Loi_De_Viabilité_Financière]], tirée de *So Good They Can't Ignore You*.
Machiavel est ce que l'inventaire a de plus proche d'une analyse institutionnelle,
et il a 513 ans.

**Le détail qui rend la lacune gênante :** [[Source-Thinking_in_Systems]] fournit le
vocabulaire des stocks, des boucles et des points de levier — [[Concept-Stock_Et_Flux]],
[[Concept-Délai_Systémique]], [[Concept-Résistance_Aux_Politiques]] — **sans un seul
système empirique de grande échelle sur lequel l'exercer.** Meadows est outillé pour
les institutions et n'a que des exemples de baignoire.

| Candidat | Ce qu'il apporte que ses voisins n'apportent pas |
|---|---|
| **Bueno de Mesquita & Smith — *The Dictator's Handbook*** (2011) | le pouvoir comme structure d'incitations d'une coalition. C'est le contrepoids **avec données** aux trois Greene : il explique *pourquoi* les manœuvres de [[Source-The_48_Laws_of_Power]] marchent quand elles marchent |
| **Scott — *Seeing Like a State*** (1998) | pourquoi la planification par le haut échoue. Taleb le cite — il est **déjà dans le réseau de citations du vault** sans être dans l'inventaire |
| **Sowell — *Basic Economics*** | les mécanismes de prix et d'incitation, sans mathématiques. Le contradicteur serait Ha-Joon Chang, *23 Things* — à prendre si on veut le débat plutôt que la doctrine |

## 3 · Le Véhicule ne contenait pas l'écriture — ✅ fermée le 2026-10-02

> **Fermée par acquisition.** *Style: Lessons in Clarity and Grace* (Williams &
> Bizup, 13ᵉ éd.) est entré dans [[Ref-Bibliothèque]] au niveau `fiché`, puis en
> **tête de la phase 2** de [[Ref-Lecture_Ordre_de_Priorité]]. Le candidat sort
> d'ici ; la lacune et sa preuve restent.

Ce qui était constaté, et qui vaut d'être gardé : phase 2, quatre titres —
Viktorovitch (rhétorique), Cabane (charisme), Carnegie (conversation), Carnegie
(prise de parole). **Les quatre étaient oraux ou interpersonnels**, et rien ne
portait sur la prose écrite, qui est le produit de sortie d'un Zettelkasten.

L'objection évidente ne tenait pas : [[Concept-Écriture_Comme_Medium]] vient
d'Ahrens et dit qu'écrire **est** le support de la pensée. C'est l'écriture comme
instrument de travail, pas comme transmission — et la phase 2 est précisément celle
de la transmission.

**Et le constat s'est renforcé en route.** La correction du domaine de
`Stage_Academy_Workbook_2024`, le même jour, a fait passer l'axe oral de quatre
actifs à cinq pendant que l'écrit en comptait toujours zéro. Une lacune peut
s'aggraver entre son relevé et sa fermeture.

**Ce qui est sorti d'ici :**

| Titre | Devenu |
|---|---|
| **Williams — *Style*** | acquis **et converti en entier** le 2026-10-02 — douze leçons · `fiché` · tête de phase 2 · **11 notes**, toutes `⬜` · [[Ref-Principes_De_Clarté]] |
| **Pinker — *The Sense of Style*** (2014) | **plus un candidat.** Il donnait le *pourquoi* linguistique des mêmes règles : sur un axe désormais couvert, c'est un second titre du même sujet, donc une décision de rendement — pas une lacune. À reprendre seulement si Williams laisse la question du *pourquoi* ouverte |

> ⚠️ **Strunk & White est Lindy et ne doit pas être pris pour autant.** Le filtre ⏳
> dit qu'un non-Lindy qui contredit un Lindy doit fournir la preuve — ici elle est
> fournie : les linguistes ont documenté que plusieurs de ses préceptes décrivent mal
> l'anglais, et que ses auteurs les violaient dans le livre même. C'est le premier cas
> du vault où le filtre ⏳ est **explicitement écarté sur preuve**, et il vaut d'être
> noté comme tel dans [[Concept-Effet_Lindy]] : *la survie n'est pas la vérité.*

## 4 · Le corps n'avait qu'un livre — ✅ fermée le 2026-10-02

> **Fermée par acquisition.** *Exercised* (Lieberman, Pantheon 2021) est entré dans
> [[Ref-Bibliothèque]] au niveau `fiché`, domaine `corps/santé`, puis en **phase 1**
> de [[Ref-Lecture_Ordre_de_Priorité]] — et non au Socle, voir plus bas.

`Corps/` contenait **5 notes atomiques et 1 fiche**. Cette fiche est
[[Source-Why_We_Sleep]], dont la liste 1 dit elle-même : *« garde les mécanismes,
jette les chiffres »*.

La phase 1 déclare acheter *« la capacité de produire »*. Elle couvre l'attention,
les habitudes, les croyances sur soi, et le sommeil. **Elle ne couvre ni le
mouvement ni l'alimentation.**

> **L'asymétrie la plus frappante de l'inventaire : le domaine qui repose sur la
> littérature la plus solide est le plus vide.** L'effet de l'exercice physique sur
> la cognition et l'humeur est parmi les mieux établis de tout ce que cette
> bibliothèque touche — et c'est le seul sujet de cette qualité sur lequel elle n'a
> rien. Les 61 verdicts `🟠 contesté` du vault viennent de sujets où la preuve est
> faible ; celui-là aurait produit des `🟢`.

**Ce qui est sorti d'ici :**

| Titre | Devenu |
|---|---|
| **Lieberman — *Exercised*** (2021) | acquis **et converti en entier** le 2026-10-02 — treize chapitres · `fiché` · `corps/santé` · **phase 1** · **9 notes**, dont 2 `🟢` · [[Ref-Activité_Et_Maladies]] |
| **Schoenfeld — *Science and Development of Muscle Hypertrophy*** | **plus un candidat de lacune.** C'est une référence : elle s'achète le jour où Lieberman pose une question à laquelle elle répond, pas sur spéculation |
| **Attia — *Outlive*** (2023) | **plus un candidat.** Il recouvre Lieberman en extrapolant davantage — exactement le défaut reproché à Walker. Sur un axe désormais couvert, c'est un doublon, pas un manque |

### Pourquoi la phase 1 et pas le Socle

**C'est le seul endroit où cette note a corrigé une erreur au lieu de la constater.**
*Why We Sleep* est au Socle, et la liste 1 reconnaît que c'est une des deux
dépendances non résolues : *« lu trop tard pour ce qu'il conditionne »*. Ranger le
mouvement à côté du sommeil aurait rangé Lieberman par **thème** — or le thème passe
en dernier, et le substrat physique est un **prérequis** de la phase 1, pas sa
conclusion.

C'est le premier emploi de la règle écrite dans [[Guide-Stratégie_Lecture]] *avant*
de lire le livre, et non après l'avoir mal placé.

**Conséquence prévisible sur les tags :** `corps/santé` était déjà déclaré et vide —
il absorbe le début. La règle des 5 (décision 03) ouvrira `corps/mouvement` si
Lieberman produit cinq notes de physiologie de l'effort, exactement comme `corps/`
est né de *Why We Sleep* et de van der Kolk.

## 5 · Aucune histoire — donc rien pour contrôler Greene

**Zéro livre d'histoire dans l'inventaire.** Or la phase 4 est entièrement bâtie sur
l'anecdote historique, et la liste 1 l'écrit noir sur blanc à propos des *48 Laws* :
*« Zéro donnée : verdict `⬜ non applicable`, valeur descriptive. »*

L'antidote à des anecdotes triées n'est pas un quatrième manuel de stratégie — ce
sont **les sources que Greene pille**.

Et ce geste est déjà posé **trois fois délibérément dans ce vault** : Goffman sous
Cabane et Navarro, Marc Aurèle sous le stoïcisme de vulgarisation, Kant parce que
*Beyond Good and Evil* §11 est illisible sans lui. **La lacune n'est donc pas un
nouveau principe, c'est le même appliqué une quatrième fois.**

| Candidat | ⏳ | Ce qu'il apporte que ses voisins n'apportent pas |
|---|---|---|
| **Thucydide — *La Guerre du Péloponnèse*** | ⏳ | là où naît le réalisme stratégique. Le dialogue des Méliens est l'énoncé le plus net du rapport de force jamais écrit, et Clausewitz comme tous les autres le lisent |
| **Plutarque — *Vies parallèles*** | ⏳ | littéralement la carrière d'où Greene extrait ses pierres. À lire par vies choisies, jamais d'un bout à l'autre |

## 6 · `tech/` — une décision à prendre, pas un trou à combler

`Tech/` contient **4 notes, toutes `⬜ non applicable`, et 1 fiche**.
[[MOC-Tech]] liste déjà ce qui lui manque. Mais la vraie question n'est pas « quels
livres ajouter » :

> **`tech/` est-il dans le périmètre de ce vault ?** Le savoir métier est
> périssable, s'apprend en faisant, et se cite mal hors de son domaine — il
> échoue au critère d'entrée de la décision 01, la **citabilité**.

**Et la réponse est déjà écrite dans [[MOC-Tech]] :** *« les meilleures notes
techniques de ce vault ne parlent pas de code »*. [[Concept-Orthogonalité]] justifie
la décision 03, [[Concept-DRY]] la source unique de [[Ref-Bibliothèque]],
[[Concept-Fenêtre_Brisée]] l'existence de l'audit.

**D'où le critère d'entrée du domaine, qui manquait :** un livre technique entre
dans `tech/` **si ses principes sont citables hors du code**. Sinon il est un outil
de travail, au même régime que `Modern_Compiler_Implementation_in_ML` — sur le
disque, hors stratégie de lecture.

À ce filtre, *Designing Data-Intensive Applications* échoue malgré son excellence —
il est excellent **en tant que** savoir métier. Et passent :

| Candidat | ⏳ | Ce qu'il apporte que ses voisins n'apportent pas |
|---|---|---|
| **Brooks — *The Mythical Man-Month*** (1975) | ⏳ | la loi de Brooks est une affirmation sur le **coût de communication d'une équipe**, pas sur le code. C'est aussi le pont vers la lacune n° 2 — et il devient Lindy cette année |
| **Ousterhout — *A Philosophy of Software Design*** (2018) | | la complexité comme adversaire unique, et une taxonomie de ses symptômes. Citable depuis n'importe quel domaine, y compris depuis ce vault |

---

## Deux remarques de proportion

Elles ne nomment aucun titre manquant : elles disent où le rayonnage est allé.

**`social/séduction` compte trois titres** — *Models*, *Mate*, *Attached* — et
c'est aussi, de l'aveu de la liste 1, le sous-domaine le plus fragile
empiriquement : *« le titre le plus contesté de la liste entière »* pour *Mate*,
*« le moins falsifiable »* pour *Models*. Trois titres là, **zéro sur l'argent,
zéro sur le mouvement**. Ce n'est pas un reproche au sous-domaine — c'est le constat
que l'inventaire a reçu ses priorités d'un ordre d'arrivée, pas d'une décision.

> ⚠️ **Ce constat était faux d'un titre, et la correction renforce la lacune n° 3.**
> `Stage_Academy_Workbook_2024` était rangé en `social/séduction` : c'est le cahier
> d'exercices de **Vinh Giang**, sur la voix et la présence à l'oral — corrigé en
> `social/charisme` le 2026-10-02. Il ne quitte pas le rayon pour un rayon vide : il
> passe du sous-domaine le plus fragile vers **l'axe oral de la phase 2**, qui compte
> donc cinq actifs quand l'écrit en compte toujours zéro.
> **Un domaine posé par défaut ne se relit pas tout seul** — c'est la troisième fois
> que ce motif se produit, après les six niveaux de périmètre jamais relus contre le
> jugement de la liste 1.

**Une source primaire est citée sans être lue.**
[[Concept-Pratique_Délibérée]] porte Ericsson, Krampe & Tesch-Römer 1993 dans sa
`fiabilite_note`, et sa `source` est [[Source-Deep_Work]]. Ericsson n'est pas dans
l'inventaire. C'est le motif exact qui a fait entrer Goffman le 2026-09-29 — la
vulgarisation fichée, le primaire absent. **Ericsson & Pool, *Peak*** (2016) le
solderait. C'est le dix-septième candidat, et le moins cher : une note existe déjà
pour l'accueillir.

---

## Comment une lacune se ferme

**Deux façons, et la seconde compte autant que la première.** C'est la leçon tirée
des huit livres `fiché` sans fiche, consignée dans [[Ref-Bibliothèque]] : *une dette
n'est pas toujours du travail à faire, c'est parfois un classement à corriger.*

| | Fermeture | Ce qu'on écrit |
|---|---|---|
| **par acquisition** | un titre est acheté | une ligne dans [[Ref-Bibliothèque]] avec son niveau et son domaine, **puis** une entrée dans la phase qui lui convient de [[Ref-Lecture_Ordre_de_Priorité]] — dans cet ordre, l'inventaire d'abord |
| **par décision** | l'axe est déclaré **hors périmètre** | la lacune reste ici, statut `fermée — hors périmètre`, avec la raison. On ne supprime pas la ligne : la faire disparaître effacerait la décision, exactement comme les trois PDF supprimés gardent leur ligne avec `💾 —` |

**La lacune n° 6 ne peut se fermer que de la seconde façon ou des deux** : le
critère de citabilité y décide d'abord si le domaine existe, et seulement ensuite
quels titres y entrent.

> ⚠️ **Cette note n'est pas une file de lecture et ne doit pas en devenir une.**
> Un candidat qui entre dans une phase de la liste 1 **sort d'ici** — sinon le même
> titre vit à deux endroits avec deux statuts, et c'est précisément la divergence que
> [[Ref-Bibliothèque]] a été créée pour supprimer. Ce qui reste dans cette note, c'est
> la **lacune**, avec sa preuve et sa date : elle survit à la fermeture, le candidat non.

### 🔗 Connexions
* [[Guide-Stratégie_Lecture]] — *les trois listes, le filtre ⏳, et la règle des instruments d'abord.*
* [[Ref-Bibliothèque]] — *l'inventaire : c'est lui qui déclare niveau et domaine, jamais cette note.*
* [[Ref-Lecture_Ordre_de_Priorité]] — *la liste 1, et les cinq phases dont les énoncés ont servi au test 2.*
* [[Guide-Conventions]] — *décision 01 pour la citabilité, 03 pour la règle des 5, 05 pour le champ dont la lacune n° 1 est l'angle mort.*
* [[MOC-Tech]] — *la section « Ce qui manque », d'où sort le critère d'entrée de la lacune n° 6.*
