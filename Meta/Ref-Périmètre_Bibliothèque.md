---
tags: [meta/ref]
---
# 📚 Périmètre de la bibliothèque

> **Référence stable, lue par le script d'audit.** Chaque PDF d'`Extras/` porte
> ici son niveau de périmètre (décision 12). C'est ce tableau qui dit à l'audit
> sur quels livres appliquer le garde-fou — et donc ce qui l'empêche de crier sur
> des livres qui n'ont rien de fautif.

Les trois niveaux, et ce qu'ils impliquent :

| Niveau | Fiche `Source-` | Notes `Concept-` | Garde-fou 11 |
|---|---|---|---|
| `fiché` | oui, mince | oui | **oui** — une fiche sans note est signalée |
| `lu-sans-fiche` | non | oui | non |
| `illustration` | oui, mince | **non** | non |
| `dehors` | non | non | non |

> ⚠️ **Le niveau `illustration` — la fiction lue pour sa structure.**
> Un roman de la liste [[Ref-Lecture_SciFi_Stratégique]] n'est ni un manuel ni du
> loisir : il **modélise** un mécanisme de pouvoir ou de système. Mais une fiction
> n'est pas une affirmation sur le monde, donc **elle ne fait naître aucun
> `Concept-`**. Elle est *citée comme exemple* depuis une note existante :
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

**Format des lignes : ne pas changer les colonnes** — le script les parse.

## Fiché — 35 titres

| PDF | Niveau | Domaine |
|---|---|---|
| Antifragile | fiché | esprit/stratégie |
| Atomic_Habits | fiché | esprit/habitudes |
| Comment_Parler_En_Public | fiché | social/influence |
| Deep_Work | fiché | esprit/productivité |
| Digital_Minimalism | fiché | esprit/productivité |
| Dressing_the_Man_Mastering_the_Art_of_Permanent_Fashion | fiché | social/style |
| Essentialism | fiché | esprit/productivité |
| How_to_Take_Smart_Notes | fiché | esprit/productivité |
| How_to_Win_Friends_and_Influence_People | fiché | social/influence |
| Le_Pouvoir_Rhétorique | fiché | social/influence |
| Make_Time_How_to_Focus | fiché | esprit/productivité |
| Mans_Search_For_Meaning | fiché | esprit/philosophie |
| Mate_Become_the_Man_Women_Want | fiché | social/séduction |
| Mindset | fiché | esprit/psychologie |
| Models | fiché | social/séduction |
| Never_Split_the_Difference | fiché | social/négociation |
| Propaganda | fiché | social/influence |
| So_Good_They_Cant_Ignore_You | fiché | esprit/productivité |
| Surrounded_by_Idiots | fiché | social/influence |
| Skin_in_the_Game | fiché | esprit/stratégie |
| The_33_Strategies_of_War | fiché | esprit/stratégie |
| The_48_Laws_of_Power | fiché | esprit/stratégie |
| The_Black_Swan | fiché | esprit/stratégie |
| The_Body_Keeps_the_Score | fiché | esprit/psychologie |
| The_Charisma_Myth | fiché | social/charisme |
| The_Happiness_Advantage | fiché | esprit/psychologie |
| The_Laws_of_Human_Nature | fiché | esprit/psychologie |
| The_ONE_Thing | fiché | esprit/productivité |
| The_Power_of_Habit | fiché | esprit/habitudes |
| The_Pragmatic_Programmer | fiché | tech/programmation |
| The_Psychology_of_Persuasion | fiché | social/influence |
| Thinking_Fast_And_Slow | fiché | esprit/biais |
| Thinking_in_Systems | fiché | esprit/stratégie |
| What_Every_Body_Is_Saying | fiché | social/influence |
| Why_We_Sleep | fiché | corps/sommeil |

`Why_We_Sleep` est le seul titre dont le domaine n'existe pas encore : `corps/`
naîtra à sa 5ᵉ note de physiologie (règle des 5). D'ici là, ses notes prennent
`esprit/psychologie` si elles portent sur la cognition, sinon elles attendent.

## Lu sans fiche — 9 titres

*Aucune thèse, aucune « action » à en tirer : exiger une fiche produirait du
remplissage. Mais ils alimentent des notes atomiques, dont le champ `source`
pointe le PDF directement.*

| PDF | Niveau | Domaine | Pourquoi |
|---|---|---|---|
| Beyond_Good_and_Evil | lu-sans-fiche | esprit/philosophie | texte primaire |
| Critique_of_Pure_Reason | lu-sans-fiche | esprit/philosophie | texte primaire |
| English_Phrasal_Verbs_in_Use_Advanced | lu-sans-fiche | langues/vocabulaire | cahier d'exercices |
| Meditations | lu-sans-fiche | esprit/philosophie | texte primaire |
| Modern_Compiler_Implementation_in_ML | lu-sans-fiche | tech/programmation | manuel de cours |
| On_War | lu-sans-fiche | esprit/stratégie | texte primaire |
| Stage_Academy_Workbook_2024 | lu-sans-fiche | social/séduction | cahier d'exercices |
| The_Art_of_War | lu-sans-fiche | esprit/stratégie | texte primaire |
| The_Prince | lu-sans-fiche | esprit/stratégie | texte primaire |

## Illustration — 4 titres

*Fiction lue pour sa structure. Fiche `Source-` mince autorisée, **aucun `Concept-`** : ces
romans sont **cités comme exemples** depuis des notes existantes. Voir
[[Ref-Lecture_SciFi_Stratégique]].*

| PDF | Niveau | Domaine | Ce qu'il modélise |
|---|---|---|---|
| Brave_New_World | illustration | esprit/stratégie | le contrôle par le plaisir plutôt que par la peur |
| We | illustration | esprit/stratégie | la transparence totale comme mécanisme de contrôle |
| 1984 | illustration | esprit/stratégie | le contrôle par la langue : rendre une pensée non formulable |
| Fahrenheit_451 | illustration | esprit/stratégie | la censure par désintérêt, non par interdiction |

## Dehors — 1 titre

| PDF | Niveau | Pourquoi |
|---|---|---|
| To_Kill_A_Mockingbird | dehors | fiction de loisir |

*Tout livre **explicitement écarté** après examen vient ici : le ficher
contredirait la décision de l'écarter.*

`To_Kill_A_Mockingbird` relève du même régime que [[Ref-Lecture_SciFi_plaisir]] :
lu pour le plaisir, hors vault, et c'est assumé.

## Les titres pas encore sur le disque

Ce tableau ne couvre que les PDF présents. **Les 34 essais de la liste de priorité sont désormais tous sur le disque.** Restent
les **30 romans** des deux listes SF, qui portent leur niveau dans leur liste :

* [[Ref-Lecture_Ordre_de_Priorité]] — 34 essais, **tous possédés**
* [[Ref-Lecture_SciFi_Stratégique]] — 18 romans, niveau `illustration`, 0 possédé
* [[Ref-Lecture_SciFi_plaisir]] — 12 romans, niveau `dehors`, 0 possédé

### 🔗 Connexions
* [[Guide-Conventions]] — *décisions 11 et 12.*
