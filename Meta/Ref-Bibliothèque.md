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
`Fichier` est le nom du PDF sans extension ; pour un titre non possédé, c'est le
**nom qu'il devra porter** à l'acquisition. `💾` dit s'il est dans `Extras/Books/`,
et l'audit recoupe cette colonne avec le disque.

## Fiché — 37 titres, 37 sur le disque

*Fiche `Source-` + notes `Concept-`. Le garde-fou 11 s'applique : une fiche sans note est signalée, et un livre fiché sans fiche est compté en dette.*

| Fichier | 💾 | Niveau | Domaine | Liste |
|---|---|---|---|---|
| Antifragile | ✅ | fiché | esprit/stratégie | priorité |
| Atomic_Habits | ✅ | fiché | esprit/habitudes | priorité |
| Attached | ✅ | fiché | social/séduction | priorité |
| Comment_Parler_En_Public | ✅ | fiché | social/influence | priorité |
| Deep_Work | ✅ | fiché | esprit/productivité | priorité |
| Digital_Minimalism | ✅ | fiché | esprit/productivité | — |
| Dressing_the_Man_Mastering_the_Art_of_Permanent_Fashion | ✅ | fiché | social/style | priorité |
| Essentialism | ✅ | fiché | esprit/productivité | priorité |
| How_to_Take_Smart_Notes | ✅ | fiché | esprit/productivité | priorité |
| How_to_Win_Friends_and_Influence_People | ✅ | fiché | social/influence | priorité |
| Le_Pouvoir_Rhétorique | ✅ | fiché | social/influence | priorité |
| Make_Time_How_to_Focus | ✅ | fiché | esprit/productivité | — |
| Mans_Search_For_Meaning | ✅ | fiché | esprit/philosophie | priorité |
| Mate_Become_the_Man_Women_Want | ✅ | fiché | social/séduction | priorité |
| Mindset | ✅ | fiché | esprit/psychologie | priorité |
| Models | ✅ | fiché | social/séduction | priorité |
| Never_Split_the_Difference | ✅ | fiché | social/négociation | priorité |
| Propaganda | ✅ | fiché | social/influence | priorité |
| Skin_in_the_Game | ✅ | fiché | esprit/stratégie | priorité |
| So_Good_They_Cant_Ignore_You | ✅ | fiché | esprit/productivité | priorité |
| Surrounded_by_Idiots | ✅ | fiché | social/influence | — |
| The_33_Strategies_of_War | ✅ | fiché | esprit/stratégie | priorité |
| The_48_Laws_of_Power | ✅ | fiché | esprit/stratégie | priorité |
| The_Black_Swan | ✅ | fiché | esprit/stratégie | priorité |
| The_Body_Keeps_the_Score | ✅ | fiché | esprit/psychologie | priorité |
| The_Charisma_Myth | ✅ | fiché | social/charisme | priorité |
| The_Happiness_Advantage | ✅ | fiché | esprit/psychologie | — |
| The_Laws_of_Human_Nature | ✅ | fiché | esprit/psychologie | priorité |
| The_ONE_Thing | ✅ | fiché | esprit/productivité | — |
| The_Power_of_Habit | ✅ | fiché | esprit/habitudes | — |
| The_Pragmatic_Programmer | ✅ | fiché | tech/programmation | priorité |
| The_Presentation_of_Self_in_Everyday_Life | ✅ | fiché | social/influence | priorité |
| The_Psychology_of_Persuasion | ✅ | fiché | social/influence | priorité |
| Thinking_Fast_And_Slow | ✅ | fiché | esprit/biais | priorité |
| Thinking_in_Systems | ✅ | fiché | esprit/stratégie | priorité |
| What_Every_Body_Is_Saying | ✅ | fiché | social/influence | priorité |
| Why_We_Sleep | ✅ | fiché | corps/sommeil | priorité |

## Lu sans fiche — 10 titres, 10 sur le disque

*Aucune thèse, aucune « action » à en tirer : exiger une fiche produirait du remplissage. Ils alimentent des notes atomiques, dont le champ `source` pointe le PDF directement.*

| Fichier | 💾 | Niveau | Domaine | Liste |
|---|---|---|---|---|
| Beyond_Good_and_Evil | ✅ | lu-sans-fiche | esprit/philosophie | priorité |
| Critique_of_Pure_Reason | ✅ | lu-sans-fiche | esprit/philosophie | — |
| English_Phrasal_Verbs_in_Use_Advanced | ✅ | lu-sans-fiche | langues/vocabulaire | — |
| Meditations | ✅ | lu-sans-fiche | esprit/philosophie | priorité |
| Modern_Compiler_Implementation_in_ML | ✅ | lu-sans-fiche | tech/programmation | — |
| On_War | ✅ | lu-sans-fiche | esprit/stratégie | priorité |
| Relations_in_Public | ✅ | lu-sans-fiche | social/influence | priorité |
| Stage_Academy_Workbook_2024 | ✅ | lu-sans-fiche | social/séduction | — |
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

## Dehors — 18 titres, 6 sur le disque

*Rien. Tout livre **explicitement écarté** après examen vient ici : le ficher contredirait la décision de l'écarter.*

| Fichier | 💾 | Niveau | Domaine | Liste |
|---|---|---|---|---|
| Cat_s_Cradle | — | dehors | — | scifi-plaisir |
| Consider_Phlebas | — | dehors | — | scifi-plaisir |
| Do_Androids_Dream_of_Electric_Sheep | — | dehors | — | scifi-plaisir |
| Forward_the_Foundation | ✅ | dehors | — | — |
| Foundation_and_Earth | ✅ | dehors | — | — |
| Foundations_Edge | ✅ | dehors | — | — |
| Jurassic_Park | — | dehors | — | scifi-plaisir |
| Old_Man_s_War | — | dehors | — | scifi-plaisir |
| Rendezvous_with_Rama | — | dehors | — | scifi-plaisir |
| Second_Foundation | ✅ | dehors | — | — |
| The_Hitchhiker_s_Guide_to_the_Galaxy | — | dehors | — | scifi-plaisir |
| The_Moon_is_a_Harsh_Mistress | — | dehors | — | scifi-plaisir |
| The_Rest_of_the_Robots | ✅ | dehors | — | — |
| The_Sirens_of_Titan | — | dehors | — | scifi-plaisir |
| The_Stars_My_Destination | — | dehors | — | scifi-plaisir |
| To_Kill_A_Mockingbird | ✅ | dehors | — | — |
| Ubik | — | dehors | — | scifi-plaisir |
| Way_Station | — | dehors | — | scifi-plaisir |

## Ce que cet inventaire fait apparaître

**16 titres du disque n'appartiennent à aucune liste de lecture** (`liste = —`).
C'est la raison pour laquelle l'inventaire ne pouvait pas être fondu dans les
trois `Ref-Lecture_*` : ils y seraient devenus sans domicile.

Par ailleurs **huit livres sont `fiché` sans avoir de fiche** — sur la liste ou non,
ils attendent en silence :

| Titre | Depuis |
|---|---|
| `Digital_Minimalism` · `Make_Time_How_to_Focus` · `Surrounded_by_Idiots` | la construction du vault |
| `The_Happiness_Advantage` · `The_ONE_Thing` · `The_Power_of_Habit` | la construction du vault |
| `Attached` · `The_Presentation_of_Self_in_Everyday_Life` | 2026-09-29 |

L'audit les compte désormais en dette. **Le garde-fou 11 ne voyait que l'inverse**
— une fiche sans note — donc huit livres pouvaient rester en attente indéfiniment
sans qu'aucun contrôle ne s'en plaigne.

> **Les cinq suites du cycle Fondation sont lues par curiosité, hors vault** —
> décision du 2026-09-28. Elles ne produisent ni fiche ni note. `To_Kill_A_Mockingbird`
> relève du même régime : lu pour le plaisir, hors vault, et c'est assumé.

### 🔗 Connexions
* [[Guide-Conventions]] — *décisions 11 et 12.*
* [[Guide-Stratégie_Lecture]] — *comment les trois listes s'articulent.*
* [[Ref-Lecture_Ordre_de_Priorité]] · [[Ref-Lecture_SciFi_Stratégique]] · [[Ref-Lecture_SciFi_plaisir]] — *l'ordre et le pourquoi.*
