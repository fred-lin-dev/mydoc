---
tags: [tech/programmation, esprit/stratégie]
source: "[[Source-The_Pragmatic_Programmer]]"
fiabilite: ⬜ non applicable
fiabilite_note: "Règle de conception : s'évalue par contre-exemple, pas par mesure."
---
# Balle traçante

## L'idée

Construire d'abord un chemin **complet mais mince** à travers tout le système —
entrée, traitement, sortie — plutôt qu'un composant parfait à la fois.

L'image vient des munitions traçantes : au lieu de calculer la trajectoire, on tire
un projectile visible et on corrige en regardant où il va. Ce qu'on cherche n'est pas
le résultat final, c'est un **retour d'information sur la trajectoire**.

La distinction avec un prototype est nette et souvent manquée : un prototype est
jetable, une balle traçante est **du code définitif**, simplement incomplet. On
l'épaissit, on ne la remplace pas.

## Ce qui la rend vraie, ou fragile

**Ce que la règle attaque :** le risque d'intégration. Un système construit composant
par composant ne révèle ses incompatibilités qu'à la fin — au moment où elles coûtent
le plus. Un chemin complet les révèle tout de suite, quand il n'y a presque rien à
défaire.

**La condition d'application :** ça suppose de connaître les extrémités du chemin. Si
l'entrée et la sortie sont elles-mêmes incertaines, on ne trace rien — on explore, et
c'est un prototype qu'il faut.

**Hors du code :** c'est la même logique que fiche mince → note atomique → carte,
appliquée à ce vault. Le premier livre fiché est passé par **toute** la chaîne avec
six notes, plutôt que de produire quarante notes sans jamais tester la synchronisation
ni l'audit. Les défauts de convention sont apparus au premier passage, pas au
quarantième.

### 🔗 Connexions
* [[Concept-Orthogonalité]] — *ce qui rend l'épaississement possible sans tout casser.*
* [[Guide-Stratégie_Lecture]] — *la procédure par livre est une balle traçante.*

## 🎴 Cartes

Q: Qu'est-ce qu'une balle traçante en conception, et quel risque attaque-t-elle ?
A: Un chemin complet mais mince à travers tout le système. Elle attaque le risque d'intégration : les incompatibilités apparaissent tout de suite, pas à la fin.
<!--ID: 1790533410628-->


Q: Quelle est la différence entre une balle traçante et un prototype ?
A: Le prototype est jetable ; la balle traçante est du code définitif, simplement incomplet. On l'épaissit, on ne la remplace pas.
<!--ID: 1790533410631-->


Q: Quand faut-il un prototype plutôt qu'une balle traçante ?
A: Quand les extrémités du chemin sont elles-mêmes incertaines. On ne peut pas tracer vers une cible inconnue.
<!--ID: 1790533410635-->

