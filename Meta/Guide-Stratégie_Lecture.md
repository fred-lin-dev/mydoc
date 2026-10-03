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
| [[Ref-Lecture_SciFi_Stratégique]] | **les exemples** — modèles de pouvoir et de systèmes. **Fiction *ou* histoire**, voir plus bas | `illustration` | fiche mince, **aucune note** |
| [[Ref-Lecture_SciFi_plaisir]] | **le plaisir** | `dehors` | rien, volontairement |

Elles sont séparées par **ce qu'elles produisent**, pas par leur qualité. Un roman
de la liste 2 peut être meilleur qu'un essai de la liste 1 — il ne produit
simplement pas la même chose.

## Le filtre Lindy — ⏳

**L'effet Lindy :** pour une chose non périssable, l'espérance de vie restante est
proportionnelle à l'âge déjà atteint. Note complète, avec sa limite décisive —
*la survie n'est pas la vérité* — dans [[Concept-Effet_Lindy]]. Un livre lu depuis cinquante ans le sera
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

### Et l'histoire entre par la même porte — 2026-10-03

**Un récit historique se lit pour ses exemples, donc il relève d'`illustration` et non
de la bibliothèque de travail.** Thucydide, Plutarque, une biographie, un récit de
campagne : ils entrent au niveau `illustration`, avec une fiche `Source-` mince, et
**ils sont cités comme exemples depuis une note existante** — exactement comme un roman.

```markdown
## Exemples
* Le dialogue des Méliens (Thucydide, V, 84-116) — les Athéniens énoncent le rapport
  de force sans l'habiller de justice : ce que la note appelle séparer le moral de
  l'efficace, dit par les intéressés eux-mêmes.
```

> **Pourquoi cette phrase existe.** [[Ref-Lecture_Lacunes]] a constaté qu'aucun livre
> d'histoire n'est dans l'inventaire, alors que la phase 4 est **entièrement bâtie sur
> l'anecdote historique**. Le tri du 2026-10-03 a retiré ses deux candidats, et la
> raison était la bonne : **ils n'apportaient aucun concept neuf.** Leur valeur est
> d'être des **exemples de contrôle** sur les anecdotes que Greene a choisies — et un
> exemple de contrôle n'a pas besoin de produire une note, il a besoin d'être
> vérifiable.

**Conséquence sur le nom de la liste 2, et elle est assumée :** son titre dit
*« SciFi »* parce que c'est ce qu'elle contient aujourd'hui, pas ce qu'elle admet. Son
périmètre est le niveau `illustration`, et le niveau ne parle pas de genre. **Un titre
historique y entre sans renommer la liste** ; s'il en arrive plusieurs, c'est la règle
des 5 qui dira s'il faut une famille à part.

> ⚠️ **La limite à ne pas franchir : un historien qui *argumente* n'est pas une
> illustration.** Tacite raconte, Scott (*Seeing Like a State*) démontre — le second
> produit des `Concept-` et appartient à la liste 1. Le test est celui de la
> décision 01 : **une thèse citable hors de son époque → `fiché` ; un récit qui sert
> d'exemple → `illustration`.**

## La procédure, par livre

1. **Vérifier le niveau** dans [[Ref-Bibliothèque]]. `dehors` → on lit,
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

**Les 41 titres de la liste 1 sont convertis.** Les deux derniers — *Style*
(Williams & Bizup) en tête de phase 2, *Exercised* (Lieberman) en phase 1 — ont été
acquis et convertis le 2026-10-02.

Et il entre par une porte neuve : c'est le premier titre venu de
[[Ref-Lecture_Lacunes]], donc d'un **axe constaté absent**, et non d'une liste
d'envies. La procédure ci-dessus ne change pas pour autant — l'inventaire d'abord,
la phase ensuite.

## Les instruments passent avant, hors phase

**Un livre qui sert à *juger* les autres ne se range pas par thème.** Le thème lui
donne une place dans la file, et cette place est toujours trop tard.

C'est la seule erreur de structure identifiée dans la liste 1, et elle est étroite :
« Le Socle » a été construit comme une phase, donc comme un thème, donc en cinquième
position — alors que son contenu est un **prérequis** des quatre autres.

**Le coût est mesuré, pas supposé.** [[Concept-Preuve_Silencieuse]] vient de
*The Black Swan*, lu en avant-dernier. Cette note est le défaut structurel de **six
livres lus avant elle** — Newport, Voss, Greene ×2, Manson, Frankl. La même remarque
a été écrite six fois à la main avant que le concept existe. Neuf notes la citent
aujourd'hui.

La liste 1 porte d'ailleurs six dépendances qui traversent ses propres phases, et
**quatre pointent de la phase 5 vers l'arrière** : *Thinking, Fast and Slow* « à
remonter en phase 1 », *Why We Sleep* « en amont de *Deep Work* », *The Body Keeps
the Score* « contrepoids de la phase 1 », *The Presentation of Self* « source
primaire de toute la phase 3 ».

**La règle, pour tout corpus à venir :**

| | |
|---|---|
| **1** | les **instruments** d'abord — ce qui sert à évaluer une affirmation, hors de toute phase |
| **2** | les **prérequis** ensuite — ce qu'un livre exige d'un autre pour être lisible |
| **3** | le **thème** en dernier, comme départage |

Le thème garde sa valeur **à l'intérieur d'un niveau** : lire plusieurs livres d'un
même sujet à la suite est ce qui fait naître les liens entre eux, et c'est ce qu'un
Zettelkasten cherche. L'erreur n'est pas de grouper — c'est de laisser un thème
décider de la position d'un instrument.

## Les pièges

* **Le collector's fallacy.** L'écart entre PDF possédés, fiches écrites et notes
  produites est le seul indicateur honnête. `Scripts/audit.py` affiche les trois en
  tête de rapport — et signale désormais les livres `fiché` **sans fiche**, qui
  étaient huit à dormir sans que rien ne le dise.
* **Ouvrir le livre suivant avant d'avoir converti le précédent.** C'est
  exactement ce que le garde-fou 11 empêche.
* **Vider la liste « dehors ».** Chaque reclassement d'un roman de plaisir vers la
  liste stratégique affaiblit la protection de l'audit. Le critère est
  « j'ai une note existante que ce roman illustre mieux », pas « ça m'a plu ».

### 🔗 Connexions
* [[Guide-Conventions]] — *les règles que cette procédure applique.*
* [[MOC-Audit]] — *l'état réel de la conversion.*
* [[Ref-Lecture_Lacunes]] — *les axes qu'aucune des trois listes ne couvre, et la preuve de leur absence.*
