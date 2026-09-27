---
tags: [meta/source, tech/programmation]
auteur: Andrew Hunt & David Thomas
annee: 1999
pdf: "[[The_Pragmatic_Programmer.pdf]]"
lu: en cours
---
# The Pragmatic Programmer

> **Fiche mince.** Le savoir vit dans les `Concept-`, pas ici.

**Thèse en une ligne.** La qualité d'un logiciel se décide dans des habitudes de
conception qui n'ont rien de technique : ne pas dupliquer le savoir, garder les
parties indépendantes, et réparer les petits défauts avant qu'ils fassent norme.

*352 pages. Le seul livre technique de la phase 1, et il y est pour sa méthode —
ses principes se citent depuis n'importe quel domaine.*

## Analyse perso

*À remplir après lecture.*



## Vérification épistémique

> **Cas particulier : ce livre n'affirme presque rien sur le monde.** Ses principes
> sont des **règles de conception**, vraies par construction ou fausses par
> contre-exemple — pas des hypothèses empiriques. La plupart de ses notes portent
> donc `⬜ non applicable`, et c'est la bonne réponse : exiger un verdict empirique
> ici produirait exactement le faux positif que dénonce la décision 07.

| Ce que le livre affirme | État réel |
|---|---|
| **DRY**, **orthogonalité**, **balles traçantes** | `⬜ non applicable` — règles de conception, évaluables par contre-exemple et non par mesure |
| **Fenêtres brisées** — réparer les petits défauts tout de suite | La **règle d'ingénierie** tient. Mais elle emprunte son autorité à la théorie criminologique de Wilson & Kelling (1982), **elle-même fortement contestée** → [[Concept-Fenêtre_Brisée]] |
| **Le canard en plastique** — expliquer à voix haute fait apparaître le trou | Même mécanisme que [[Concept-Reformulation_Comme_Test]], déjà dans le vault. **Pas de note nouvelle** : ajouté comme exemple |

## Actions

- [ ] Appliquer DRY au vault lui-même : un fait, un endroit. `Ref-Périmètre_Bibliothèque` est la seule source de vérité des niveaux
- [ ] Traiter toute incohérence de convention comme une fenêtre brisée : la réparer le jour où on la voit

### 🔗 Notes atomiques issues de ce livre
* [[Concept-DRY]] — *un savoir, une représentation autoritaire.*
* [[Concept-Orthogonalité]] — *changer une chose ne doit pas en changer une autre.*
* [[Concept-Balle_Traçante]] — *un chemin complet et mince avant un composant parfait.*
* [[Concept-Fenêtre_Brisée]] — *le petit défaut toléré devient la norme.*

### 🔗 Notes déjà dans le vault, citées sans duplication
* [[Concept-Reformulation_Comme_Test]] — *le canard en plastique, sous son nom générique.*
