---
tags: [meta/ref]
---
# 🕳️ Lacunes — les axes que la bibliothèque ne couvre pas

> **Référence stable : la liste des sujets absents, et la preuve de leur absence.**
> Les trois `Ref-Lecture_*` disent quoi lire et dans quel ordre. Celle-ci dit
> **ce qui n'est sur aucune des trois** — et pourquoi on le sait.
>
> Établie le **2026-10-02**, quand les titres de
> [[Ref-Lecture_Ordre_de_Priorité]] étaient tous convertis et qu'aucune liste de
> lecture n'avait plus de file. C'est le moment où la question se pose : une
> bibliothèque sans file n'est pas une bibliothèque complète, c'est une
> bibliothèque dont on ne connaît plus les bords.
>
> **Relue sur le vault le 2026-10-03.** Les trois tests ont été relancés, les six
> lacunes vérifiées une par une, et le test 1 a été relancé **à l'échelle** au lieu
> d'un terme à la main — il en sort deux lacunes de plus et une preuve beaucoup plus
> dure pour la première. Rien n'a été supprimé : les deux fermetures tiennent, et la
> mécanique de la note a fonctionné exactement comme elle était écrite.

> ⚠️ **Les numéros sont des identifiants, pas un rang.** `MOC-Corps`,
> `MOC-Social`, `Ref-Lecture_Ordre_de_Priorité` et `Guide-Conventions` renvoient aux
> lacunes **par leur numéro** — les renuméroter casserait ces renvois. Une lacune
> nouvelle prend donc le numéro suivant, et la gravité se lit dans le tableau, pas
> dans l'ordre.

**Cette note ne déclare ni niveau de périmètre ni domaine.** Un titre candidat n'a
pas encore de traitement — il en reçoit un dans [[Ref-Bibliothèque]] **le jour où il
est acquis**, et pas avant. Les porter ici les ferait divarier comme les
`Ref-Lecture_*` avaient commencé à le faire.

| | | |
|---|---|---|
| lacunes retenues | **8** | 3 ouvertes · 2 à trancher · **3 fermées** |
| titres candidats | **7** | 13 avant le tri du 2026-10-03 ; aucun n'est engagé |
| candidats écartés | **6** | leur concept central est **déjà une note du vault** — voir le filtre 4 |
| dont *Lindy* ⏳ | **2** | Popper et Brooks — Thucydide et Plutarque sont sortis au filtre 4 |
| lacunes fermées | **3** | n° 3 et 4 **par acquisition** le 2026-10-02 · n° 5 **par décision** le 2026-10-03 |
| notes produites par les deux | **20** · 59 cartes | Williams 11 · 32 · Lieberman 9 · 27 |
| ajoutées le 2026-10-03 | **n° 7 et n° 8** | la première par le test 1 relancé à l'échelle, la seconde par le test 3 |

---

## Comment une lacune a été établie

C'est la partie de cette note qui ne se reconstitue pas depuis le vault : **trois
tests, et un sujet n'entre ici que s'il en passe au moins un.** Sans ça, « il
manque des livres » est une opinion sans fin — on peut toujours en nommer un.

| | Test | Ce qu'il attrape |
|---|---|---|
| **1** | **Le vocabulaire sans source.** Un terme que les notes emploient pour juger, mais qu'aucun livre de l'inventaire n'enseigne. Mesuré par `grep` | les lacunes **n° 1 et n° 7** — et aucune des deux ne pouvait être trouvée autrement |
| **2** | **La phase contre son propre énoncé.** Chaque phase de la liste 1 déclare *ce qu'elle achète*. On compare à ce qu'elle contient | les lacunes **n° 3, 4, 5** |
| **3** | **La place occupée.** Combien de titres pour un sous-domaine, zéro pour un autre. Le rayonnage est une déclaration de priorité, qu'on l'ait voulu ou non | les lacunes **n° 2, 6** et les deux remarques de proportion |

**Ce que les trois tests ont en commun :** ils se mesurent **sur le vault**, pas sur
une idée de ce qu'une bibliothèque devrait contenir. Un sujet qui ne passe aucun des
trois n'est pas une lacune — c'est un livre que quelqu'un a envie de recommander.

> ⚠️ **Le test 1 est le seul qui ne dépende de la discipline de personne**, comme
> `fiabilite_date` parmi les contrôles d'audit. Les tests 2 et 3 demandent un
> jugement ; celui-là se relance avec un `grep` et répond seul.

### Le filtre 4 — un candidat dont le concept est déjà écrit n'est pas un candidat

**Ajouté le 2026-10-03, et il s'applique après les trois autres.** Les trois tests
établissent qu'un **axe** manque. Ils ne disent rien du **titre** qu'on met dessus — et
c'est là que les candidats s'accumulaient. La règle :

> **Un candidat ne reste que si le concept central qu'il apporterait n'a pas déjà sa
> note `Concept-`.** Sinon on n'achète pas une lacune, on rachète ce qu'on a lu.

C'est la version « bibliothèque » du test de citabilité : le critère n'est plus *« ce
sujet est-il absent ? »* mais *« ce livre fait-il apparaître une note qui n'existe
pas ? »*. Appliqué aux treize candidats, il en retire six :

| Candidat écarté | Ce qu'il apporterait | La note qui l'a déjà |
|---|---|---|
| **Ericsson & Pool — *Peak*** | la pratique délibérée | [[Concept-Pratique_Délibérée]] — **elle existe depuis le début, et c'est elle qui citait Ericsson**. Le candidat le moins cher était en fait le plus inutile |
| **Sowell — *Basic Economics*** | *« pas de solutions, que des arbitrages »* | [[Concept-Arbitrage_Inévitable]], qui le dit déjà et mieux — un arbitrage est la structure de la situation, pas un échec d'optimisation |
| **Ousterhout — *A Philosophy of Software Design*** | la complexité et ses symptômes | [[Concept-Orthogonalité]] et [[Concept-DRY]] en portent l'essentiel, et c'est tout ce que `tech/` sait rendre citable |
| **Thucydide — *La Guerre du Péloponnèse*** | le rapport de force nu | [[Concept-Séparer_Moral_Et_Efficace]] — Machiavel porte déjà la séparation du juste et de l'efficace |
| **Plutarque — *Vies parallèles*** | rien : des **exemples** | aucune note à produire par construction. C'est de l'`illustration`, régime de [[Ref-Lecture_SciFi_Stratégique]], pas de la bibliothèque de travail |
| **Todorov — *Face Value*** | le jugement en une fraction de seconde | [[Concept-Proportion_Avant_Qualité]] **cite déjà Willis & Todorov 2006**, et n'est pas contestée. Rien à réparer |

> ⚠️ **Le filtre 4 ne ferme aucune lacune — il vide des files.** Les axes n° 2, 5 et 6
> restent absents ; ils ont simplement moins de titres en face, et ceux qui restent sont
> ceux dont on peut nommer la note qu'ils produiront. **Une lacune sans candidat reste
> une lacune**, et c'est le cas de la n° 5 depuis ce tri.

### Le test 1 relancé à l'échelle — 2026-10-03

**Le 2026-10-02, le test 1 avait été appliqué à un terme choisi à la main** (*Popper*),
et il avait suffi à établir la lacune la plus grave. Rien n'obligeait à s'arrêter là :
le champ `fiabilite_note` cite ses appuis en clair, donc la liste des auteurs sur
lesquels le vault s'appuie **s'extrait**, et se croise avec l'inventaire.

```bash
# tous les appuis cités, dédupliqués par patronyme
grep -rh "^fiabilite_note:" --include='*.md' . \
  | grep -oE "[A-ZÉÀ][A-Za-zéèêëïöüçñ'-]+( ?[&,] ?[A-ZÉÀ][A-Za-zéèêëïöüçñ'-]+)*,? (et al\.?,? )?(19|20)[0-9]{2}" \
  | sort -u                          # 124 références
# puis, réduit au patronyme :
  | cut -d' ' -f1 | sed 's/,$//' | sort -u   # 115 auteurs
```

> ✅ **Vérifié le 2026-10-03 : la commande ci-dessus reproduit les deux chiffres.**
> C'est une exigence et pas une politesse — une preuve qu'on ne peut pas relancer
> n'est plus une preuve six mois plus tard, c'est une affirmation.

| | |
|---|---|
| références distinctes citées | **124** |
| patronymes distincts | **115** |
| notes qui en portent au moins une | **163** — c'est-à-dire **toutes** les `Concept-` |
| patronymes ayant un livre dans [[Ref-Bibliothèque]] | **2** — Kahneman et Roediger, et personne d'autre |

> ⚠️ **Le croisement brut en annonçait treize : onze étaient des homonymes.**
> *Miller 1990* est Danny Miller et son *Icarus Paradox*, pas le Geoffrey Miller de
> *Mate*. *Torre & Lieberman 2018* est Matthew Lieberman, pas le Daniel Lieberman
> d'*Exercised*. *Williams, Bourgeois & Croyle 1993* n'est pas le Williams de *Style*.
> **Un test mécanique sur des patronymes mélange les gens** — il faut lire les onze
> lignes avant de garder le chiffre, et c'est la limite du test 1.

> **Le vault juge avec une littérature qu'il ne peut pas lire.** Ce n'est pas une
> liste de cent treize livres à acheter : des articles ne s'achètent pas comme des livres, et
> la plupart ne sont cités qu'une fois, pour un point précis, déjà réglé par la
> vérification. **Ce qui est une lacune, c'est l'appui qui revient** — un auteur cité
> trois fois contre trois livres différents n'est plus une note de bas de page, c'est
> un pilier absent de l'étagère.

Les appuis qui reviennent, et ce qu'ils portent :

| Appui | × | Contre quoi il est invoqué | Statut |
|---|---|---|---|
| **Dunlosky et al. 2013** | 5 | les techniques d'étude du vault lui-même | **soldé** — *Make It Stick*, acquis le 2026-10-02, est écrit par Roediger |
| **Brehm 1966 · Rains 2013** | 3 + 3 | Voss, Carnegie, la modalisation — la réactance psychologique | ouvert, lacune **n° 7** |
| **DePaulo et al. 2003 · Barrett et al. 2019** | 2 + 2 | Navarro et Cabane — le non-verbal comme lecture d'état interne | ouvert, lacune **n° 7** |
| **Sisk et al. 2018 · Maier et al. 2022** | 2 + 2 | Dweck — la taille réelle de l'effet du *mindset* | ouvert, lacune **n° 1** — et **rien à acheter** : ce sont des méta-analyses, pas des livres. Ce qui manque n'est pas un titre, c'est de savoir les lire |

**Et c'est ce tableau qui a produit la lacune n° 7**, qu'aucun jugement n'aurait
trouvée : personne ne se dit « il me manque un livre sur l'émotion ». Le `grep`, lui,
montre que **deux des quatre appuis récurrents du vault contestent le même rayon**.

---

## Les huit lacunes, par gravité

**Preuves revérifiées sur le vault le 2026-10-03.** Quand un chiffre a bougé, les deux
sont donnés : celui du relevé et celui d'aujourd'hui. C'est la seule façon de voir si
une lacune se comble ou s'aggrave — et aucune ne s'est comblée toute seule.

| # | Lacune | La preuve, prise dans le vault | Statut |
|---|---|---|---|
| **1** | **Méthodologie de la preuve** | `grep -rni "popper"` → **0**, toujours. `grep -rli "méta-analyse\|taille d'effet\|réplicat"` → 57 → **59 fichiers** | ouverte, **aggravée** |
| **7** | **La littérature qui corrige `social/`** | 4 appuis récurrents, **0 livre** ; 29 `🟠` + 4 `🔴` sur **61** notes `Social/`, et **2 `🟢`** | ouverte — *nouvelle, 2026-10-03* |
| **2** | **Argent et institutions** | toujours **1 seule note** dont l'argent est le sujet — [[Concept-Loi_De_Viabilité_Financière]], et elle vient de Newport en passant. **143 notes** au relevé, **163** aujourd'hui, et toujours une seule | ouverte, **aggravée** |
| **5** | **L'histoire** | **0 titre**, alors que la phase 4 est bâtie sur l'anecdote historique et le dit : *« zéro donnée »* | **fermée — hors périmètre**, 2026-10-03 : l'axe relève d'`illustration` |
| **6** | **`tech/`** | **4 notes, toutes `⬜`** — inchangé depuis le relevé, alors que le vault a gagné 0 note technique en une semaine | **à trancher**, voir plus bas |
| **8** | **`langues/`** | **0 note**, un dossier vide, deux sous-tags déclarés, et **un actif classé `lu-sans-fiche`** — un niveau qui promet des notes | **à trancher** — *nouvelle, 2026-10-03* |
| **3** | **L'écriture** | phase 2, 4 titres, **4 oraux ou interpersonnels** | **fermée** — 2026-10-02 |
| **4** | **Le corps au-delà du sommeil** | `Corps/` = **5 notes, 1 fiche** — et c'était [[Source-Why_We_Sleep]], le plus critiqué de la liste | **fermée** — 2026-10-02 |

> **Le fait le plus net de cette relecture : depuis le relevé, le vault a gagné
> 143 → 163 notes, et les vingt viennent toutes des deux lacunes fermées.** Zéro
> ailleurs. Donc une lacune **ne se comble pas par croissance** — rien n'est arrivé par
> accident dans `tech/`, dans `langues/`, ni sur l'argent — et cette note est
> actuellement **le seul endroit du vault qui décide où il grossit**. Les deux
> fermetures ne sont pas deux acquisitions parmi d'autres : ce sont les seules.
>
> Ce qui rend l'aggravation lisible : une lacune ouverte **reste exactement là où elle
> était** pendant que le reste avance. Il fallait une seconde mesure pour le voir, et
> c'est la raison de garder les deux chiffres dans la colonne de preuve.

---

## 1 · L'instrument empirique n'est pas dans la bibliothèque

**C'est la lacune qui se démontre toute seule.**

```
grep -rni "popper"                                          → 0 occurrence   (inchangé)
grep -rli "méta-analyse|taille d'effet|réplicat|p-hacking"  → 59 fichiers   (57 au relevé)
```

**Et l'instrument s'est alourdi entre les deux mesures.** Le 2026-10-02, le champ
`fiabilite` a reçu une sixième valeur, `🔵 invérifiable` — *on a cherché, rien
n'existe* — et une date obligatoire sur tout verdict tranché, avec un horizon de
24 mois. Le vault compte aujourd'hui **97 verdicts datés**, dont 70 `🟠`, 20 `🟢`,
5 `🔴` et 4 `🔵`.

> La valeur `🔵` est **exactement** la distinction que Popper sert à faire : une
> affirmation pour laquelle aucun dispositif ne trancherait n'est pas une affirmation
> faible, c'est une affirmation d'une autre nature. Elle a été ajoutée par nécessité
> pratique, après quatre dettes qu'aucune recherche ne pouvait solder — **sans que le
> livre qui la théorise soit dans la bibliothèque.** L'écart entre l'outil et sa
> théorie s'est creusé, pas réduit.

Tout l'appareil `fiabilite` (décision 05) est un **critère de falsifiabilité
appliqué**, et aucun livre de l'inventaire ne l'enseigne. Les sept verdicts fragiles
de la liste 1 citent Sisk 2018, Maier 2022, Macnamara 2014, Guzey 2019 — c'est-à-dire
la littérature de la crise de la réplication, **utilisée comme outil sans avoir été
lue comme sujet**.

**Une partie de la lacune a été payée, et il faut le dire.** Le relevé reprochait à
*Dunlosky et al. 2013* d'être « utilisée comme outil sans avoir été lue comme sujet ».
C'est réglé : *Make It Stick* est entré le 2026-10-02 et son auteur, Roediger, **est**
le chercheur de l'effet de test. C'est le seul des quatre appuis récurrents du vault
qui ait désormais un livre derrière lui — et c'est aussi la preuve que ce genre de
dette **se solde par un titre bien choisi, pas par une bibliothèque entière**.

Le Socle contient la *philosophie* de la connaissance : Kant pour les limites du
savoir, Nietzsche pour l'origine des valeurs, Taleb pour les queues et
[[Concept-Preuve_Silencieuse]]. Il ne contient pas la *méthode* de l'évidence.

**Et par la règle de [[Guide-Stratégie_Lecture]] — « les instruments d'abord, hors
phase » — c'est exactement le type de livre qui ne devrait pas pouvoir manquer.**
La règle a été écrite après avoir constaté que le Socle arrivait trop tard. Elle
n'avait pas encore servi à constater qu'il était **incomplet**.

| Candidat | ⏳ | Ce qu'il apporte que ses voisins n'apportent pas |
|---|---|---|
| **Popper — *Conjectures and Refutations*** (1963) | ⏳ | **la falsifiabilité** — le critère que le champ `fiabilite` applique tous les jours sans l'avoir écrit une fois. Primaire, et Lindy, même raison que Goffman et Marc Aurèle |
| **Ritchie — *Science Fictions*** (2020) | | **le biais de publication et le `p`-hacking.** Le vault emploie « taille d'effet » dans 59 fichiers et n'a aucune note qui dise ce que c'est ni comment on la gonfle |
| **Pearl — *The Book of Why*** (2018) | | **la confusion** (*confounding*) et l'inférence causale. Le vault n'a que « corrélation ≠ causalité » comme sagesse populaire, et aucune note pour l'outiller |

> **Le plus urgent des sept.** Il manque **sous** le vault, pas à côté : c'est le
> seul candidat dont l'absence affecte la fiabilité de tout ce qui est déjà écrit.

## 7 · La littérature qui corrige le vault n'est pas dans le vault

> **Nouvelle le 2026-10-03, trouvée par le test 1 relancé à l'échelle.** C'est la
> lacune n° 1 appliquée à un rayon précis : non pas « il manque la méthode de la
> preuve », mais **« il manque les livres qui contredisent ceux qu'on a lus »**.

`Social/` est le rayon le plus fourni du vault et le plus fragile de loin :

| | |
|---|---|
| notes `Social/` | **61** |
| dont `🟠 contesté` | **29** |
| dont `🔴 réfuté` | **4** |
| dont `🟢 solide` | **2** |

**Et les 33 notes fragiles se répartissent sur 13 sources différentes** — 5 chez Voss,
4 chez Cabane, 4 chez Manson, 3 chez Navarro, 3 chez Carnegie, et ainsi de suite.
Ce n'est donc pas un mauvais livre à retirer : **c'est le rayon qui est bâti sur de la
vulgarisation**, et le constat ne se répare pas en jetant un titre.

Ce qui a tranché ces 33 verdicts n'est dans aucun de ces livres. Deux appuis reviennent :

| Appui récurrent | × | Ce qu'il réfute ou limite | Le livre qui le porte |
|---|---|---|---|
| **Barrett et al. 2019**, *Psych. Sci. Public Interest* 20(1) | 2 | les configurations faciales ne correspondent pas de façon fiable à des catégories d'émotion — ni entre individus, ni entre cultures. C'est ce qui met [[Concept-État_Interne_Fuit]] et [[Concept-Signal_D_Inconfort]] en `🟠` | **absent** |
| **Brehm 1966** + méta-analyse **Rains 2013** | 3 + 3 | la réactance psychologique : le seul mécanisme bien étayé sous trois notes de persuasion — [[Concept-Modalisation]], [[Concept-Éviter_La_Discussion]], [[Concept-Question_Calibrée]] | **absent** |

> **Le motif est celui qui a fait entrer Goffman, puis Kant, puis Make It Stick :
> la vulgarisation est fichée, le primaire est absent.** La différence ici, c'est que
> le primaire n'est pas *sous* le livre lu — il est **contre** lui. Goffman fondait
> Cabane ; Barrett le démolit. Un vault qui ne range que des fondations n'a aucun
> moyen de se contredire tout seul.

| Candidat | ⏳ | La note qu'il ferait apparaître, et qui n'existe pas |
|---|---|---|
| **Barrett — *How Emotions Are Made*** (2017) | | **l'émotion construite** : il n'y a pas de catégories émotionnelles universelles que le visage trahirait, mais une construction par le cerveau à partir du contexte. Le vault n'a aucune note là-dessus — et il a [[Concept-Cerveau_Triunique]], que Barrett démolit frontalement. **Un seul livre touche 7 notes déjà écrites** : 4 chez Cabane, 3 chez Navarro |

**Le seul candidat qui reste, et c'est voulu.** *Face Value* de Todorov et *Detecting
Lies and Deceit* de Vrij sont sortis au filtre 4 : le premier parce que son appui est
déjà cité dans une note non contestée, le second parce que
[[Concept-Détection_Du_Mensonge]] est déjà `🔴 réfuté` avec trois méta-analyses. **Une
lacune ne se mesure pas sur ce qui est déjà tranché** — seulement sur ce qui juge sans
appui.

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

| Candidat | La note qu'il ferait apparaître, et qui n'existe pas |
|---|---|
| **Bueno de Mesquita & Smith — *The Dictator's Handbook*** (2011) | **la taille de la coalition gagnante.** Le vault a déjà [[Concept-Pouvoir_Conféré]] — le pouvoir est prêté — et [[Concept-Levier_Des_Minorités_Organisées]] — une minorité organisée bat une majorité dispersée. **Ce qu'aucune des deux ne dit : que le *nombre* de ceux qu'il faut payer détermine le comportement du régime.** C'est le contrepoids avec données aux trois Greene |
| **Scott — *Seeing Like a State*** (1998) | **la lisibilité imposée.** Pour gouverner, on simplifie d'abord ce qu'on gouverne — et c'est la simplification qui casse, pas l'intention. [[Concept-Iatrogénie]] dit que l'intervention nuit, [[Concept-Résistance_Aux_Politiques]] qu'elle est absorbée ; **aucune ne dit pourquoi la mesure précède le dégât.** Taleb le cite : il est déjà dans le réseau du vault sans être dans l'inventaire |

**Sowell, *Basic Economics*, est sorti au filtre 4** : sa thèse centrale — *« il n'y a
pas de solutions, seulement des arbitrages »* — est déjà [[Concept-Arbitrage_Inévitable]],
et mieux formulée là-bas.

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

**Ce qui a fermé la lacune :** *Style* de Williams, acquis **et converti en entier** le
2026-10-02 — douze leçons · `fiché` · tête de phase 2 · **11 notes** · 32 cartes ·
[[Ref-Principes_De_Clarté]].

*Pinker, **The Sense of Style**, n'est plus un candidat : sur un axe couvert, un second
titre du même sujet est une décision de rendement, pas une lacune.*

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

**Ce qui a fermé la lacune :** *Exercised* de Lieberman, acquis **et converti en
entier** le 2026-10-02 — treize chapitres · `fiché` · `corps/santé` · **phase 1** ·
**9 notes**, dont 2 `🟢` · 27 cartes · [[Ref-Activité_Et_Maladies]].

*Schoenfeld (**Muscle Hypertrophy**) et Attia (**Outlive**) ne sont plus des candidats :
le premier est une référence, qui s'achète le jour où Lieberman pose une question à
laquelle elle répond ; le second recouvre Lieberman en extrapolant davantage — le défaut
exact reproché à Walker.*

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

## 5 · Aucune histoire — ✅ fermée le 2026-10-03, hors périmètre

> **Fermée par décision, et c'est la première de ce type.** Les n° 3 et 4 s'étaient
> fermées par acquisition. Celle-ci se ferme parce que **l'axe n'appartient pas à cette
> note** : il relève du niveau `illustration`, et la règle est désormais écrite dans
> [[Guide-Stratégie_Lecture]] — *« l'histoire entre par la même porte »*. La lacune
> garde sa ligne et sa preuve ; elle n'attend plus d'achat.

**Zéro livre d'histoire dans l'inventaire.** Or la phase 4 est entièrement bâtie sur
l'anecdote historique, et la liste 1 l'écrit noir sur blanc à propos des *48 Laws* :
*« Zéro donnée : verdict `⬜ non applicable`, valeur descriptive. »*

L'antidote à des anecdotes triées n'est pas un quatrième manuel de stratégie — ce
sont **les sources que Greene pille**.

Et ce geste est déjà posé **trois fois délibérément dans ce vault** : Goffman sous
Cabane et Navarro, Marc Aurèle sous le stoïcisme de vulgarisation, Kant parce que
*Beyond Good and Evil* §11 est illisible sans lui. **La lacune n'est donc pas un
nouveau principe, c'est le même appliqué une quatrième fois.**

### Le filtre 4 a vidé cette file, et c'est le résultat le plus instructif du tri

**Les deux candidats sont sortis le 2026-10-03, pour deux raisons différentes.**

| Candidat écarté | Pourquoi |
|---|---|
| **Thucydide** | le concept qu'on en tirerait — le rapport de force nu, le dialogue des Méliens — **est déjà** [[Concept-Séparer_Moral_Et_Efficace]], que Machiavel a produit |
| **Plutarque** | il ne produit aucun concept **par construction** : ce sont des vies, c'est-à-dire des exemples. C'est de l'`illustration` |

> **Donc la lacune est réelle et n'a aucun candidat — et ce n'est pas une contradiction.**
> L'axe manquant n'est pas un concept absent : c'est un **jeu d'exemples de contrôle**
> pour vérifier les anecdotes de Greene. Or le vault range les exemples au niveau
> `illustration` — fiche mince, **aucune note** — et au régime de
> [[Ref-Lecture_SciFi_Stratégique]], pas de la bibliothèque de travail.
>
> **Ce que ça révèle : l'histoire ne relève pas de cette note.** Aucun achat de la
> liste 1 ne couvrira l'axe ; c'était une lacune de **structure des listes**, pas de
> contenu de la bibliothèque.
>
> ✅ **Et la phrase a été écrite le 2026-10-03** dans [[Guide-Stratégie_Lecture]], section
> *« Et l'histoire entre par la même porte »* : un récit historique relève
> d'`illustration`, fiche mince, aucune note, cité comme exemple depuis une note
> existante — avec la limite qui va avec, **un historien qui argumente n'est pas une
> illustration** : Tacite raconte, Scott démontre, et Scott est en lacune n° 2.
>
> **Donc la lacune se ferme sans rien acheter**, et c'est le seul cas où un tri de
> candidats a produit une décision de méthode au lieu d'une liste de courses.

## 6 · `tech/` — une décision à prendre, pas un trou à combler

`Tech/` contient **4 notes, toutes `⬜ non applicable`** — le même chiffre qu'au
relevé, après une semaine où le vault en a gagné vingt ailleurs — plus deux fiches,
dont une est [[Source-I_Robot]], une `illustration` qui par construction ne produit
rien.
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

| Candidat | ⏳ | La note qu'il ferait apparaître, et qui n'existe pas |
|---|---|---|
| **Brooks — *The Mythical Man-Month*** (1975) | ⏳ | **le coût de communication croît plus vite que l'équipe.** Ajouter des gens à un projet en retard le retarde davantage — une affirmation sur les équipes, pas sur le code, et le vault n'a rien dessus. C'est aussi le pont vers la lacune n° 2, et il devient Lindy cette année |

**Ousterhout, *A Philosophy of Software Design*, est sorti au filtre 4** : la complexité
et ses symptômes, c'est ce que [[Concept-Orthogonalité]] et [[Concept-DRY]] portent déjà
— et c'est tout ce que `tech/` sait rendre citable hors du code.

## 8 · `langues/` — déclaré, promis, vide

> **Nouvelle le 2026-10-03, trouvée par le test 3.** C'est la lacune n° 6 un cran plus
> loin : `tech/` est *quasi* vide et a le mérite d'avoir produit quatre notes utiles.
> `langues/` n'a jamais rien produit du tout.

```
Langues/                          0 fichier — le dossier est littéralement vide
Guide-Conventions, décision 03    langues/ → anglais, vocabulaire     (déclaré)
Ref-Bibliothèque                  English_Phrasal_Verbs_in_Use_Advanced
                                  niveau lu-sans-fiche · langues/vocabulaire
Guide-Méthode_Zettelkasten l. 98  un exemple de note tagguée langues/anglais
```

**Ce qui en fait une lacune et pas un simple vide : le niveau déclaré.**
`lu-sans-fiche` veut dire *pas de fiche, mais des notes* — c'est le seul des quatre
niveaux qui promette des `Concept-` sans rien pour le vérifier, puisque le garde-fou 11
ne surveille que `fiché`. Le titre est donc **classé dans un niveau qu'il ne remplit
pas**, et rien ne l'a signalé. C'est le même motif que les huit `fiché` sans fiche :
*une dette n'est pas toujours du travail à faire, c'est parfois un classement à
corriger.*

> ⚠️ **Et la correction ne va pas de soi, parce que l'argument de la décision 01 coupe
> dans les deux sens.** Un *phrasal verb* échoue à la **citabilité** — « take after »
> ne se cite depuis aucun autre domaine, exactement comme le savoir métier de la
> lacune n° 6. Mais [[Guide-Méthode_Zettelkasten]] donne un exemple de note de
> vocabulaire, et [[Ref-Lecture_Ordre_de_Priorité]] a gardé le cahier au motif que
> *« le supprimer fermerait un domaine avant son ouverture »*. **Le vault a donc écrit
> deux fois qu'il voulait ce domaine, et zéro fois une note dedans.**

**Les trois issues, et aucune n'est « acheter un livre » :**

| Issue | Ce qu'on écrit |
|---|---|
| **hors périmètre** | `langues/` sort de la taxonomie, le cahier passe `dehors`, la lacune reste ici avec sa raison. **C'est l'issue cohérente avec la décision 01** |
| **périmètre réduit** | on garde `langues/` mais pour les faits *sur* la langue — étymologie, faux-amis, registre — qui se citent, eux. Le vocabulaire brut reste un outil de travail, pas une note |
| **ouverture** | une première note, et la règle des 5 fait le reste. À ne choisir que si l'anglais devient un chantier, pas pour faire exister un dossier |

> **Une lacune `à trancher` est aussi une lacune.** Les n° 6 et 8 ne demandent aucun
> achat : elles demandent une phrase dans [[Guide-Conventions]]. Et tant qu'elle n'est
> pas écrite, le vault déclare deux domaines qu'il ne nourrit pas — ce qui est
> exactement ce que [[Concept-Fenêtre_Brisée]] prédit.

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

**Les sources primaires sont citées sans être lues — et ce n'était pas un cas, c'est
la règle.** La remarque d'origine ne nommait qu'un exemple :
[[Concept-Pratique_Délibérée]] porte *Ericsson, Krampe & Tesch-Römer 1993* dans sa
`fiabilite_note` et sa `source` est [[Source-Deep_Work]] — la vulgarisation fichée, le
primaire absent, le motif exact qui a fait entrer Goffman le 2026-09-29.

Le test 1 relancé à l'échelle le 2026-10-03 montre que **ce cas est le cas général** :
124 références citées, 115 auteurs, **2 avec un livre dans l'inventaire**. Ericsson
n'était pas une exception à corriger, c'était le premier exemplaire repéré d'une classe.

> **Et la conclusion change avec l'échelle.** Un cas isolé appelle un achat ; cent
> treize n'appellent pas cent treize achats. Ce qui reste vrai, c'est le **critère** :
> on achète l'appui qui **revient**, parce qu'un auteur invoqué trois fois contre trois
> livres n'est plus une référence, c'est une dépendance. Les quatre appuis récurrents
> sont identifiés plus haut, un est soldé, trois ne le sont pas.

**Et c'est pourquoi *Peak* d'Ericsson & Pool n'est plus un candidat du tout.** Le
2026-10-02 il était présenté comme « le moins cher de tous : une note existe déjà pour
l'accueillir ». Au filtre 4, cette phrase se retourne : **une note existe déjà, donc le
concept est déjà là.** [[Concept-Pratique_Délibérée]] est écrite, sourcée, et porte
Ericsson dans sa `fiabilite_note` — acheter *Peak* ne ferait apparaître aucune note
neuve, seulement un appui direct sous une note qui tient déjà.

> **Le détail qui vaut la peine d'être gardé : c'était le candidat le plus facile à
> justifier, et c'est le premier que le filtre 4 a éliminé.** « Le moins cher » et
> « le plus inutile » décrivaient le même titre, et il a fallu un critère explicite
> pour voir que c'était la même phrase.

---

## Comment une lacune se ferme

**Deux façons, et la seconde compte autant que la première.** C'est la leçon tirée
des huit livres `fiché` sans fiche, consignée dans [[Ref-Bibliothèque]] : *une dette
n'est pas toujours du travail à faire, c'est parfois un classement à corriger.*

| | Fermeture | Ce qu'on écrit |
|---|---|---|
| **par acquisition** | un titre est acheté | une ligne dans [[Ref-Bibliothèque]] avec son niveau et son domaine, **puis** une entrée dans la phase qui lui convient de [[Ref-Lecture_Ordre_de_Priorité]] — dans cet ordre, l'inventaire d'abord |
| **par décision** | l'axe est déclaré **hors périmètre** | la lacune reste ici, statut `fermée — hors périmètre`, avec la raison. On ne supprime pas la ligne : la faire disparaître effacerait la décision, exactement comme les trois PDF supprimés gardent leur ligne avec `💾 —` |

**Les lacunes n° 6 et n° 8 ne peuvent se fermer que de la seconde façon ou des
deux** : le critère de citabilité y décide d'abord si le domaine existe, et seulement
ensuite quels titres y entrent. Ce sont les deux seules de la liste qui ne coûtent
rien et qui ne peuvent pas se régler en lisant.

> **Un troisième cas, apparu le 2026-10-03 : la fermeture partielle.** *Dunlosky et
> al. 2013* était l'un des quatre appuis récurrents de la lacune n° 1 ; *Make It Stick*
> l'a soldé sans refermer la lacune, qui tient par Popper. **On l'écrit dans la preuve,
> pas dans le statut** — une lacune reste `ouverte` tant qu'il lui manque son titre
> principal, sinon le statut devient un sentiment.

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
* [[MOC-Social]] — *le rayon dont la lacune n° 7 mesure la fragilité : 33 notes `🟠` ou `🔴` sur 61.*
* [[Guide-Méthode_Zettelkasten]] — *l'exemple de note `langues/` qui n'a jamais eu de suite, et dont la lacune n° 8 tire sa moitié d'argument.*
