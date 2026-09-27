---
tags: [tech/programmation, esprit/stratégie]
source: "[[Source-The_Pragmatic_Programmer]]"
fiabilite: ⬜ non applicable
fiabilite_note: "La règle d'ingénierie est une règle, pas une hypothèse. MAIS son autorité rhétorique est empruntée à la théorie criminologique de Wilson & Kelling 1982, elle-même fortement contestée : Harcourt & Ludwig 2006, University of Chicago Law Review 73(1), 271-320, ne trouvent pas de soutien dans les données de New York ni dans une expérience sur cinq villes. Ne jamais citer l'analogie comme une preuve."
---
# Fenêtre brisée

## L'idée

Un défaut petit et toléré ne reste pas petit : il **déplace la norme**. Une fois
qu'une incohérence est visible et acceptée, la suivante coûte moins cher à accepter,
et la dégradation devient le régime normal du système.

D'où la règle : réparer le petit défaut **le jour où on le voit**, pas quand on aura
le temps. Ce qu'on répare n'est pas le défaut, c'est le signal qu'il envoie.

## Ce qui la rend vraie, ou fragile

**La règle d'ingénierie tient**, et pour une raison indépendante de toute
psychologie : dans un système où tout est propre, un défaut est **visible**. Dans un
système qui en compte déjà trente, le trente-et-unième est indétectable. La propreté
n'est pas une vertu, c'est un **dispositif de détection**.

> ⚠️ **L'analogie, en revanche, ne prouve rien.** Hunt et Thomas emprunte l'image à
> la théorie criminologique des « vitres brisées » (Wilson & Kelling, 1982), en la
> citant comme un fait établi. Elle ne l'est pas : la réanalyse des données de New
> York et une expérience conduite sur cinq villes ne lui trouvent pas de soutien.
> La règle logicielle survit sans elle — l'argument d'autorité, non.

**C'est exactement le cas prévu par la décision 07 :** la note porte
`⬜ non applicable` parce qu'elle énonce une règle de conception, et son champ de
fiabilité sert à consigner que **sa justification emprunée est fausse**. Les deux
informations cohabitent sans se contredire.

**Application directe à ce vault :** une convention violée une fois est une fenêtre
brisée. C'est la raison d'être de l'audit — il rend les défauts visibles avant qu'ils
deviennent le régime normal.

### 🔗 Connexions
* [[Concept-Orthogonalité]] — *ce qui permet de réparer localement sans tout toucher.*
* [[MOC-Audit]] — *le dispositif de détection, dans ce vault.*

## 🎴 Cartes

Q: Pourquoi faut-il réparer un petit défaut immédiatement ?
A: Parce qu'il déplace la norme : une fois une incohérence acceptée, la suivante coûte moins cher. Et parce que dans un système propre un défaut est visible — la propreté est un dispositif de détection.
<!--ID: 1790533410612-->


Q: Quel est le problème avec l'analogie des « vitres brisées » utilisée par Hunt et Thomas ?
A: Ils citent la théorie criminologique de Wilson & Kelling comme établie. Elle ne l'est pas : réanalyses et expérience sur cinq villes ne lui trouvent pas de soutien. La règle logicielle survit sans elle.
<!--ID: 1790533410617-->

