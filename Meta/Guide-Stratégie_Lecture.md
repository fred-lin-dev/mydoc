---
tags: [meta/guide]
---
# 🧭 Stratégie de lecture

> **Procédure.** Trois listes, trois rôles distincts, un seul pipeline. Ce qui est
> théorique est dans [[Guide-Méthode_Zettelkasten]] ; ce qui est règle est dans
> [[Guide-Conventions]]. Ici : ce qu'on fait, dans l'ordre.

## Les trois listes et pourquoi elles ne se mélangent pas

| Liste | Rôle | Périmètre | Produit |
|---|---|---|---|
| [[Ref-Lecture_Ordre_de_Priorité]] | **la pratique** — ce qui change ce que tu fais | `fiché` · `lu-sans-fiche` | fiches + notes atomiques |
| [[Ref-Lecture_SciFi_Stratégique]] | **les exemples** — modèles de pouvoir et de systèmes | `illustration` | fiche mince, **aucune note** |
| [[Ref-Lecture_SciFi_plaisir]] | **le plaisir** | `dehors` | rien, volontairement |

Elles sont séparées par **ce qu'elles produisent**, pas par leur qualité. Un roman
de la liste 2 peut être meilleur qu'un essai de la liste 1 — il ne produit
simplement pas la même chose.

## Le filtre Lindy — ⏳

**L'effet Lindy :** pour une chose non périssable, l'espérance de vie restante est
proportionnelle à l'âge déjà atteint. Un livre lu depuis cinquante ans le sera
probablement cinquante ans encore ; un livre de l'an dernier ne dit rien.

**Le seuil retenu ici : publié il y a plus de cinquante ans et toujours lu.**

> ⚠️ **Lindy n'est pas une liste, c'est une colonne.** Le filtre traverse les trois
> listes : *Meditations* (180) et *The Art of War* (-500) sont Lindy ; *Snow Crash*
> (1992) ne l'est pas, quelle que soit sa qualité. Baptiser une liste « Canon
> Lindy » mélange le critère et son résultat.

**À quoi ça sert concrètement.** Quand deux livres disent la même chose, le Lindy
gagne — il a déjà survécu à la sélection. Et quand un titre non-Lindy contredit un
Lindy, c'est le non-Lindy qui doit fournir la preuve.

## La règle qui protège le vault : une fiction n'engendre pas de concept

Une fiction n'est pas une affirmation sur le monde. Elle **ne fait naître aucun
`Concept-`** : elle est citée comme exemple depuis une note qui existe déjà.

```markdown
## Exemples
* *I, Robot* (Asimov 1950) — trois règles claires, un comportement conforme aux
  règles et absurde au regard de l'intention.
```

Sans cette règle, « *Dune* m'a appris que le pouvoir est X » devient une note
atomique sans base empirique, et le champ `fiabilite` cesse de vouloir dire quoi
que ce soit. C'est le seul point où les trois listes pourraient se contaminer.

## La procédure, par livre

1. **Vérifier le niveau** dans [[Ref-Périmètre_Bibliothèque]]. `dehors` → on lit,
   on ne produit rien, on s'arrête là.
2. **`fiché` → créer la fiche** depuis `Template-Source`, nommée sur le **titre
   exact du PDF** : `Source-Deep_Work` ↔ `Deep_Work.pdf`. Elle reste mince.
3. **Lire en notant les idées candidates**, pas en résumant. Le test d'entrée est
   la **citabilité** : cette idée est-elle citable depuis un autre domaine ?
4. **Écrire les `Concept-`** depuis `Template-Concept`. Verdict `⚪ non évalué` par
   défaut — la dette est assumée, pas cachée.
5. **Écrire les cartes** sous `## 🎴 Cartes`. Plus de trois sur des angles
   différents → la note contient plus d'une idée, la scinder.
6. **Relier** : la fiche liste ses notes, les notes citent la fiche. Une fiche sans
   note déclenche le garde-fou.
7. **Lancer l'audit** avant de passer au livre suivant :
   ```bash
   python3 Scripts/audit.py
   ```

## L'ordre de travail

**Liste 1 dans l'ordre, puis liste 2.** La raison n'est pas le goût : un roman
n'illustre rien tant que le concept n'existe pas dans le vault. Lire *Foundation* avant
*Thinking in Systems*, c'est avoir un exemple sans rien à illustrer.

Prochain livre : **How to Take Smart Notes** — Ahrens, sur le disque, niveau
`fiché`. C'est la méthode dont ce vault descend : la lire en premier rend tous les
suivants capitalisables.

## Les pièges

* **Le collector's fallacy.** 37 PDF, 0 fiche, 0 note : l'écart entre ces trois
  chiffres est le seul indicateur honnête. `Scripts/audit.py` les affiche à chaque
  lancement, en tête de rapport.
* **Ouvrir le livre suivant avant d'avoir converti le précédent.** C'est
  exactement ce que le garde-fou 11 empêche.
* **Vider la liste « dehors ».** Chaque reclassement d'un roman de plaisir vers la
  liste stratégique affaiblit la protection de l'audit. Le critère est
  « j'ai une note existante que ce roman illustre mieux », pas « ça m'a plu ».

### 🔗 Connexions
* [[Guide-Conventions]] — *les règles que cette procédure applique.*
* [[MOC-Audit]] — *l'état réel de la conversion.*
