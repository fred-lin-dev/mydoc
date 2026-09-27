---
tags: [tech/programmation, esprit/stratégie]
source: "[[Source-The_Pragmatic_Programmer]]"
fiabilite: ⬜ non applicable
fiabilite_note: "Règle de conception : s'évalue par contre-exemple, pas par mesure."
---
# Orthogonalité

## L'idée

Deux parties d'un système sont orthogonales si **modifier l'une ne change rien à
l'autre**. Le mot vient de la géométrie : deux axes indépendants, dont on peut
bouger un sans déplacer l'autre.

Ce que ça achète n'est pas l'élégance, c'est la **localité des conséquences**. Dans
un système orthogonal, l'effet d'un changement est borné et prévisible ; dans un
système couplé, tout changement est un pari sur ce qui va casser ailleurs.

## Ce qui la rend vraie, ou fragile

**Pourquoi c'est structurel :** ce n'est pas une préférence esthétique. Le nombre
d'interactions possibles entre parties couplées croît comme le carré de leur nombre.
Le couplage ne rend pas les choses « moins propres », il rend le raisonnement
impossible passé une certaine taille.

**Ce qui limite la règle :** l'orthogonalité parfaite coûte de l'indirection, et
l'indirection coûte de la lisibilité. Un système entièrement découplé devient
illisible d'une autre manière — on ne voit plus ce qui parle à quoi.

**Où elle s'applique hors du code, et c'est l'exemple qui a décidé ce vault :** la
décision 03 sépare **dossier**, **tag** et **lien** parce que chacun répond à une
question distincte — où la note vit, de quoi elle parle, à quoi elle se rattache. Si
un seul mécanisme portait les trois, changer le rangement changerait le sens. Les
trois sont orthogonaux, et c'est pour ça qu'ils peuvent évoluer séparément.

### 🔗 Connexions
* [[Concept-DRY]] — *la règle complémentaire : unifier ce qui doit l'être, séparer ce qui doit l'être.*
* [[Concept-Tâches_Verrouillées]] — *le même principe appliqué à l'attention : une tâche par créneau.*
* [[Guide-Conventions]] — *décision 03, l'application directe.*

## 🎴 Cartes

Q: Que signifie que deux parties d'un système sont orthogonales ?
A: Modifier l'une ne change rien à l'autre. L'effet d'un changement est borné et prévisible.
<!--ID: 1790533410599-->


Q: Pourquoi le couplage devient-il rapidement ingérable, structurellement ?
A: Le nombre d'interactions possibles croît comme le carré du nombre de parties couplées. Ce n'est pas une question de propreté mais de possibilité de raisonner.
<!--ID: 1790533410604-->


Q: Quel est le coût de l'orthogonalité poussée trop loin ?
A: De l'indirection, donc de la lisibilité : on ne voit plus ce qui parle à quoi.
<!--ID: 1790533410608-->

