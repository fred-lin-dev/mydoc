---
tags: [meta/ref]
---
# 📚 Bibliothèque

> **Inventaire unique, lu par le script d'audit.** Un titre est déclaré **ici et
> nulle part ailleurs** : son niveau de périmètre (décision 12), son domaine, sa
> présence sur le disque, et la liste de lecture d'où il vient.
>
> Les trois `Ref-Lecture_*` disent l'**ordre** et le **pourquoi** — ce qu'elles
> seules savent dire. Elles ne redisent plus ni le niveau ni le domaine : c'était
> une duplication, et elle avait déjà commencé à divarier sur les noms
> (*De la guerre* ici, `On_War` là).

Les quatre niveaux, et ce qu'ils impliquent :

| Niveau | Fiche `Source-` | Notes `Concept-` | Garde-fou 11 |
|---|---|---|---|
| `fiché` | oui, mince | oui | **oui** — une fiche sans note est signalée |
| `lu-sans-fiche` | non | oui | non |
| `illustration` | oui, mince | **non** | non |
| `dehors` | non | non | non |

> ⚠️ **Le niveau `illustration` — la fiction lue pour sa structure.**
> Un roman n'est ni un manuel ni du loisir : il **modélise** un mécanisme de pouvoir
> ou de système. Mais une fiction n'est pas une affirmation sur le monde, donc
> **elle ne fait naître aucun `Concept-`**. Elle est *citée comme exemple* depuis une
> note existante :
>
> ```markdown
> ## Exemples
> * *Foundation* (Asimov 1951) — la psychohistoire prédit les masses et échoue
>   sur un individu : la limite exacte du modèle.
> ```
>
> Sa fiche `Source-` mince sert à tracer **quels concepts elle illustre**. Sans
> cette règle, « Dune m'a appris que le pouvoir est X » devient une note atomique
> sans base empirique — et le champ `fiabilite` ne veut plus rien dire.

**Colonnes, dans cet ordre — le script les parse. Ne pas les réarranger.**
`Fichier` est le nom du fichier **sans extension** ; pour un titre non possédé, c'est
le **nom qu'il devra porter** à l'acquisition. `💾` dit s'il est dans `Extras/Books/`,
et l'audit recoupe cette colonne avec le disque.

> **Le format n'est pas la règle.** La décision 02 exige que `Source-<titre>` ↔
> `<titre>.<ext>` reste une transformation mécanique — pas que l'extension soit
> `.pdf`. `Exercised` est arrivé en **EPUB** le 2026-10-02, et c'est `audit.py` qui
> a dû apprendre à le voir (`FORMATS_LIVRE`), pas le nommage qui a dû plier.
> **Conséquence à ne pas oublier : un EPUB n'a pas de pagination stable.** Les
> citations d'un titre EPUB se font par **chapitre et intertitre**, jamais par page —
> sinon le champ `fiabilite_note` devient invérifiable, ce que les avertissements
> d'édition de Goffman et de Williams cherchaient précisément à empêcher.

## Fiché — 34 titres, 34 sur le disque

*Fiche `Source-` + notes `Concept-`. Le garde-fou 11 s'applique : une fiche sans note est signalée, et un livre fiché sans fiche est compté en dette.*

| Fichier | 💾 | Niveau | Domaine | Liste |
|---|---|---|---|---|
| Antifragile | ✅ | fiché | esprit/stratégie | priorité |
| Atomic_Habits | ✅ | fiché | esprit/habitudes | priorité |
| Attached | ✅ | fiché | social/séduction | priorité |
| Comment_Parler_En_Public | ✅ | fiché | social/influence | priorité |
| Deep_Work | ✅ | fiché | esprit/productivité | priorité |
| Dressing_the_Man_Mastering_the_Art_of_Permanent_Fashion | ✅ | fiché | social/style | priorité |
| Essentialism | ✅ | fiché | esprit/productivité | priorité |
| Exercised | ✅ | fiché | corps/santé | priorité |
| How_to_Take_Smart_Notes | ✅ | fiché | esprit/productivité | priorité |
| How_to_Win_Friends_and_Influence_People | ✅ | fiché | social/influence | priorité |
| Le_Pouvoir_Rhétorique | ✅ | fiché | social/influence | priorité |
| Make_It_Stick | ✅ | fiché | esprit/psychologie | priorité |
| Mans_Search_For_Meaning | ✅ | fiché | esprit/philosophie | priorité |
| Mate_Become_the_Man_Women_Want | ✅ | fiché | social/séduction | priorité |
| Mindset | ✅ | fiché | esprit/psychologie | priorité |
| Models | ✅ | fiché | social/séduction | priorité |
| Never_Split_the_Difference | ✅ | fiché | social/négociation | priorité |
| Propaganda | ✅ | fiché | social/influence | priorité |
| Skin_in_the_Game | ✅ | fiché | esprit/stratégie | priorité |
| So_Good_They_Cant_Ignore_You | ✅ | fiché | esprit/productivité | priorité |
| Style_Lessons_in_Clarity_and_Grace | ✅ | fiché | social/influence | priorité |
| The_33_Strategies_of_War | ✅ | fiché | esprit/stratégie | priorité |
| The_48_Laws_of_Power | ✅ | fiché | esprit/stratégie | priorité |
| The_Black_Swan | ✅ | fiché | esprit/stratégie | priorité |
| The_Body_Keeps_the_Score | ✅ | fiché | esprit/psychologie | priorité |
| The_Charisma_Myth | ✅ | fiché | social/charisme | priorité |
| The_Laws_of_Human_Nature | ✅ | fiché | esprit/psychologie | priorité |
| The_Pragmatic_Programmer | ✅ | fiché | tech/programmation | priorité |
| The_Presentation_of_Self_in_Everyday_Life | ✅ | fiché | social/influence | priorité |
| The_Psychology_of_Persuasion | ✅ | fiché | social/influence | priorité |
| Thinking_Fast_And_Slow | ✅ | fiché | esprit/biais | priorité |
| Thinking_in_Systems | ✅ | fiché | esprit/stratégie | priorité |
| What_Every_Body_Is_Saying | ✅ | fiché | social/influence | priorité |
| Why_We_Sleep | ✅ | fiché | corps/sommeil | priorité |

## Lu sans fiche — 9 titres, 9 sur le disque

*Aucune thèse, aucune « action » à en tirer : exiger une fiche produirait du remplissage. Ils alimentent des notes atomiques, dont le champ `source` pointe le PDF directement.*

| Fichier | 💾 | Niveau | Domaine | Liste |
|---|---|---|---|---|
| Beyond_Good_and_Evil | ✅ | lu-sans-fiche | esprit/philosophie | priorité |
| Critique_of_Pure_Reason | ✅ | lu-sans-fiche | esprit/philosophie | priorité |
| Meditations | ✅ | lu-sans-fiche | esprit/philosophie | priorité |
| Modern_Compiler_Implementation_in_ML | ✅ | lu-sans-fiche | tech/programmation | — |
| On_War | ✅ | lu-sans-fiche | esprit/stratégie | priorité |
| Relations_in_Public | ✅ | lu-sans-fiche | social/influence | priorité |
| Stage_Academy_Workbook_2024 | ✅ | lu-sans-fiche | social/charisme | — |
| The_Art_of_War | ✅ | lu-sans-fiche | esprit/stratégie | priorité |
| The_Prince | ✅ | lu-sans-fiche | esprit/stratégie | priorité |

## Illustration — 19 titres, 7 sur le disque

*Fiction lue pour sa structure. Fiche `Source-` mince autorisée, **aucun `Concept-`** : ces romans sont **cités comme exemples** depuis des notes existantes. Ce qu'ils modélisent est écrit dans [[Ref-Lecture_SciFi_Stratégique]], pas ici.*

| Fichier | 💾 | Niveau | Domaine | Liste |
|---|---|---|---|---|
| 1984 | ✅ | illustration | esprit/stratégie | scifi-strat |
| Blindsight | — | illustration | — | scifi-strat |
| Brave_New_World | ✅ | illustration | esprit/stratégie | scifi-strat |
| Children_of_Time | — | illustration | — | scifi-strat |
| Dune | — | illustration | — | scifi-strat |
| Ender_s_Game | — | illustration | — | scifi-strat |
| Fahrenheit_451 | ✅ | illustration | esprit/stratégie | scifi-strat |
| Foundation | ✅ | illustration | esprit/stratégie | scifi-strat |
| Foundation_and_Empire | ✅ | illustration | esprit/stratégie | scifi-strat |
| Hyperion | — | illustration | — | scifi-strat |
| I_Robot | ✅ | illustration | tech/programmation | scifi-strat |
| Neuromancer | — | illustration | — | scifi-strat |
| Snow_Crash | — | illustration | — | scifi-strat |
| Solaris | — | illustration | — | scifi-strat |
| The_Dispossessed | — | illustration | — | scifi-strat |
| The_Player_of_Games | — | illustration | — | scifi-strat |
| The_Three_Body_Problem | — | illustration | — | scifi-strat |
| The_Traitor_Baru_Cormorant | — | illustration | — | scifi-strat |
| We | ✅ | illustration | esprit/stratégie | scifi-strat |

## Dehors — 25 titres, 7 sur le disque

*Rien. Tout livre **explicitement écarté** après examen vient ici : le ficher contredirait la décision de l'écarter.*

| Fichier | 💾 | Niveau | Domaine | Liste |
|---|---|---|---|---|
| Cat_s_Cradle | — | dehors | — | scifi-plaisir |
| Consider_Phlebas | — | dehors | — | scifi-plaisir |
| Digital_Minimalism | — | dehors | esprit/productivité | — |
| Do_Androids_Dream_of_Electric_Sheep | — | dehors | — | scifi-plaisir |
| English_Phrasal_Verbs_in_Use_Advanced | ✅ | dehors | — | — |
| Forward_the_Foundation | ✅ | dehors | — | — |
| Foundation_and_Earth | ✅ | dehors | — | — |
| Foundations_Edge | ✅ | dehors | — | — |
| Jurassic_Park | — | dehors | — | scifi-plaisir |
| Make_Time_How_to_Focus | — | dehors | esprit/productivité | — |
| Old_Man_s_War | — | dehors | — | scifi-plaisir |
| Rendezvous_with_Rama | — | dehors | — | scifi-plaisir |
| Second_Foundation | ✅ | dehors | — | — |
| Surrounded_by_Idiots | — | dehors | social/influence | — |
| The_Hitchhiker_s_Guide_to_the_Galaxy | — | dehors | — | scifi-plaisir |
| The_Happiness_Advantage | — | dehors | esprit/psychologie | — |
| The_Moon_is_a_Harsh_Mistress | — | dehors | — | scifi-plaisir |
| The_ONE_Thing | — | dehors | esprit/productivité | — |
| The_Power_of_Habit | — | dehors | esprit/habitudes | — |
| The_Rest_of_the_Robots | ✅ | dehors | — | — |
| The_Sirens_of_Titan | — | dehors | — | scifi-plaisir |
| The_Stars_My_Destination | — | dehors | — | scifi-plaisir |
| To_Kill_A_Mockingbird | ✅ | dehors | — | — |
| Ubik | — | dehors | — | scifi-plaisir |
| Way_Station | — | dehors | — | scifi-plaisir |

## Ce que cet inventaire fait apparaître

**12 titres du disque n'appartiennent à aucune liste de lecture** (`liste = —`).
C'est la raison pour laquelle l'inventaire ne pouvait pas être fondu dans les
trois `Ref-Lecture_*` : ils y seraient devenus sans domicile.

### Huit livres `fiché` dormaient sans fiche — soldé le 2026-10-01

Le garde-fou 11 ne contrôlait qu'un sens : *une fiche doit produire une note*. Rien
ne vérifiait qu'un **livre `fiché` a une fiche**, donc huit pouvaient attendre
indéfiniment. Le contrôle a été ajouté le 2026-09-29, et la dette est soldée — mais
**pas comme on s'y attendait** :

| Livre | Réglé par | Pourquoi |
|---|---|---|
| `Attached` · `The_Presentation_of_Self_in_Everyday_Life` | une fiche écrite | ils la méritaient |
| `The_ONE_Thing` · `Make_Time_How_to_Focus` · `Digital_Minimalism` | **reclassés `dehors`** | redondance pure avec *Deep Work* et *Essentialism*, déjà lus |
| `The_Power_of_Habit` · `Surrounded_by_Idiots` · `The_Happiness_Advantage` | **reclassés `lu-sans-fiche`**, puis **supprimés le 2026-10-03** | le reclassement pariait sur « un apport propre qui vaut une note ». Deux jours plus tard, après lecture : **les apports étaient des doublons de concepts déjà dans le vault**, et les trois sont passés `dehors` avec `💾 —`. Voir plus bas |

**La leçon vaut plus que la dette.** Six de ces huit livres étaient au niveau le plus
lourd alors que [[Ref-Lecture_Ordre_de_Priorité]] les jugeait *« doublons »*,
*« candidat 🔴 »*, *« candidat 🟠 »* — depuis le premier jour. Le niveau avait été
posé par défaut et jamais relu contre le jugement porté ailleurs.

**Une dette n'est pas toujours du travail à faire : c'est parfois un classement à
corriger.** Et rien dans l'audit ne peut distinguer les deux — il voit qu'une fiche
manque, pas qu'elle n'aurait jamais dû être attendue.

### `English_Phrasal_Verbs` passe `dehors` sans quitter le disque — 2026-10-03

**`💾` reste à `✅` : le PDF n'est pas supprimé.** Le niveau ne dit pas si un livre est
utile, il dit **ce qu'il produit dans le Zettelkasten** — et celui-ci n'y produira rien.

| | |
|---|---|
| avant | `lu-sans-fiche` · `langues/vocabulaire` — un niveau qui **promet des notes** |
| après | `dehors` · domaine `—` — lu pour soi, hors vault. *Le sous-tag `langues/anglais` a été supprimé de la taxonomie avec le renommage en `Lexique/` : un livre hors vault n'appartient à aucun domaine de savoir.* |
| ce qu'il alimente | **`Drills/Anglais/`**, créé le 2026-10-03 : du matériel d'entraînement, exclu de `Scripts/audit.py` |

**Le motif de conservation du 2026-10-01 a été honoré, puis est devenu caduc.** Ce
jour-là, le cahier avait été gardé parce qu'il était *« l'unique actif de `langues/`, qui
est vide — le supprimer fermerait un domaine avant son ouverture »*. Le domaine a été
ouvert le 2026-10-03, **et son critère d'entrée a exclu ce livre** : un mot n'entre que
s'il remplace une périphrase déjà employée, et « take after » ne remplace rien.

> **Ce n'est pas un revirement, c'est la conclusion de l'argument.** Le cahier avait été
> gardé *pour* que le domaine puisse s'ouvrir ; il s'est ouvert, et il s'est ouvert sur
> autre chose. L'entraînement en anglais existe — dans `Drills/`, avec son propre deck
> Anki — mais pas dans le Zettelkasten, où la citabilité le refuse.

### Trois titres `lu-sans-fiche` supprimés — 2026-10-03

**Le niveau `lu-sans-fiche` promet des notes et rien ne le vérifie.** Le garde-fou 11
ne contrôle que `fiché` : un titre peut rester ici indéfiniment sans produire une seule
`Concept-`, et l'audit ne dira rien. Un comptage à la main le 2026-10-03 a trouvé
**6 des 13 à zéro note**. Trois sont des outils de travail — un cahier d'exercices ne
produit pas de note, c'est normal. Les trois autres étaient des essais :

| Titre | 💾 | Ce qui a tranché |
|---|---|---|
| `The_Power_of_Habit` | **—** | doublon d'*Atomic Habits*. Le pari de 2026-10-01 était que les habitudes **organisationnelles** lui seraient propres ; à la lecture, non |
| `The_Happiness_Advantage` | **—** | doublon de psychologie positive. Le pari était une note sur les tailles d'effet ; le vault en a déjà le motif ailleurs |
| `Surrounded_by_Idiots` | **—** | modèle DISC, sans soutien psychométrique. Le pari était une réfutation à valeur défensive ; elle n'apporte aucun concept neuf |

> **Ce qui est instructif, c'est que le pari était explicite et daté.** Le 2026-10-01
> ces trois titres ont été gardés **pour** une note précise, nommée dans
> [[Ref-Lecture_Ordre_de_Priorité]]. Deux jours plus tard, la lecture a dit non. Un
> niveau `lu-sans-fiche` posé sur une intention est **une dette déguisée en
> classement** — et il n'y a aucun moyen de savoir laquelle des deux c'est avant
> d'avoir lu.

**Les lignes restent avec `💾 —`**, comme les trois PDF supprimés le 2026-10-01 : la
décision survit, les octets non. Même statut que les 24 romans non acquis.

> **Les cinq suites du cycle Fondation sont lues par curiosité, hors vault** —
> décision du 2026-09-28. Elles ne produisent ni fiche ni note. `To_Kill_A_Mockingbird`
> relève du même régime : lu pour le plaisir, hors vault, et c'est assumé.

### 🔗 Connexions
* [[Guide-Conventions]] — *décisions 11 et 12.*
* [[Guide-Stratégie_Lecture]] — *comment les trois listes s'articulent.*
* [[Ref-Lecture_Ordre_de_Priorité]] · [[Ref-Lecture_SciFi_Stratégique]] · [[Ref-Lecture_SciFi_plaisir]] — *l'ordre et le pourquoi.*
