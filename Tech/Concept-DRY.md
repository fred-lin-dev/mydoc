---
tags: [tech/programmation, esprit/stratégie]
source: "[[Source-The_Pragmatic_Programmer]]"
fiabilite: ⬜ non applicable
fiabilite_note: "Règle de conception, pas affirmation sur le monde : elle s'évalue par contre-exemple, pas par mesure. Formulation d'origine : Hunt & Thomas 1999, « Don't Repeat Yourself »."
---
# DRY

## L'idée

*Don't Repeat Yourself.* **Chaque élément de savoir doit avoir une seule
représentation autoritaire** dans un système.

La formulation exacte compte, et elle est plus large qu'on ne croit : il ne s'agit
pas d'éviter les lignes de texte identiques, mais d'éviter que **la même décision
soit inscrite à deux endroits**. Deux blocs de code identiques par coïncidence ne
violent pas DRY ; deux endroits qui doivent changer ensemble le violent, même s'ils
ne se ressemblent pas.

## Ce qui la rend vraie, ou fragile

**Pourquoi c'est une règle et pas une hypothèse :** la duplication ne « tend pas à
causer » des incohérences, elle les **rend possibles**. Deux copies d'une décision
peuvent diverger ; une seule ne peut pas. C'est structurel.

**Le coût réel de la règle, que le livre sous-estime :** unifier deux choses qui se
ressemblent aujourd'hui mais évolueront séparément crée un couplage faux. C'est le
défaut symétrique — et il est plus difficile à défaire qu'une duplication. Le test
n'est pas « est-ce que ça se ressemble » mais **« est-ce que ça doit changer
ensemble »**.

**Où elle s'applique hors du code :** partout où une décision est écrite.
[[Ref-Périmètre_Bibliothèque]] est la seule source des niveaux de périmètre de ce
vault ; le script d'audit la lit au lieu de contenir sa propre copie de la liste.
Si les deux existaient, elles divergeraient.

### 🔗 Connexions
* [[Concept-Orthogonalité]] — *la propriété complémentaire : DRY unifie ce qui doit l'être, l'orthogonalité sépare ce qui doit l'être.*
* [[Guide-Conventions]] — *une convention écrite deux fois est une convention qui divergera.*

## 🎴 Cartes

Q: Quelle est la formulation exacte de DRY, et pourquoi est-elle plus large qu'« éviter le code dupliqué » ?
A: Chaque élément de savoir a une seule représentation autoritaire. Ce qui compte n'est pas la ressemblance, c'est que la même décision soit inscrite à deux endroits.
<!--ID: 1790533410621-->


Q: Quel est le test pour savoir s'il faut unifier deux morceaux qui se ressemblent ?
A: « Est-ce qu'ils doivent changer ensemble ? » Si non, les unifier crée un couplage faux — plus dur à défaire qu'une duplication.
<!--ID: 1790533410625-->

