---
tags: [meta/moc]
---
# 🩺 Tableau de bord du vault

> **Dataview affiche ce qui se lit dans le frontmatter, en direct.** Ce qu'il ne
> sait pas voir — liens morts, doublons de nom, frontmatter cassé, restes de
> template, tags terminés par `/` — est du ressort de `Scripts/audit.py` :
>
> ```bash
> python3 Scripts/audit.py            # rapport complet
> python3 Scripts/audit.py --erreurs  # erreurs seules
> ```
>
> C'est aussi le script qui donne les trois chiffres de conversion de la
> décision 11 : PDF / fiches / fiches ayant produit une note.
>
> *Cette note est un index : elle n'explique rien et ne porte aucune carte (04).*

---

## 1 · La file de vérification — dette triée par utilité

*La dette de fiabilité est assumée (décision 06). Elle se paie par **ordre
d'utilité**, jamais par ordre d'arrivée : la note la plus citée d'abord.*

```dataview
TABLE WITHOUT ID
  file.link AS "Note",
  length(file.inlinks) AS "Cité par",
  source AS "Source"
FROM "Esprit" OR "Social" OR "Tech" OR "Langues"
WHERE startswith(file.name, "Concept-") AND contains(fiabilite, "non évalué")
SORT length(file.inlinks) DESC
```

## 2 · Verdicts sans référence — doit rester vide

*Un verdict sans sa référence est un avis, pas une information (décision 05).*

```dataview
TABLE WITHOUT ID file.link AS "Note", fiabilite AS "Verdict"
FROM "Esprit" OR "Social" OR "Tech" OR "Langues"
WHERE startswith(file.name, "Concept-")
  AND (contains(fiabilite, "solide") OR contains(fiabilite, "contesté")
       OR contains(fiabilite, "réfuté"))
  AND (!fiabilite_note OR fiabilite_note = "")
```

## 3 · Notes sans carte de révision

*Toléré en dette, à condition que l'audit le réclame (décision 08). Écrire une
note sans en tirer de question, c'est faire du surlignage sophistiqué.*

```dataview
TABLE WITHOUT ID file.link AS "Note", fiabilite AS "Verdict"
FROM "Esprit" OR "Social" OR "Tech" OR "Langues"
WHERE startswith(file.name, "Concept-") AND !contains(file.content, "## 🎴 Cartes")
```

## 4 · Le garde-fou — fiches sans aucune note atomique

*Un livre fiché doit produire au moins un `Concept-` (décision 11). C'est ce qui
transforme la bibliothèque en file d'attente plutôt qu'en collection.*

```dataview
TABLE WITHOUT ID file.link AS "Fiche", auteur AS "Auteur", lu AS "Lu le"
WHERE startswith(file.name, "Source-")
  AND !contains(string(file.inlinks), "Concept-")
```

## 5 · Orphelines — aucun lien entrant

*Une note que rien ne cite n'est pas fautive. Mais si elle le reste, c'est qu'elle
n'a jamais servi — et son idée n'était peut-être pas citable (décision 01).*

```dataview
TABLE WITHOUT ID file.link AS "Note", file.folder AS "Domaine"
FROM "Esprit" OR "Social" OR "Tech" OR "Langues"
WHERE length(file.inlinks) = 0
SORT file.mtime ASC
```

## 6 · Répartition des verdicts

*Si tout est vert, le vert ne signale plus rien.*

```dataview
TABLE WITHOUT ID fiabilite AS "Verdict", length(rows) AS "Notes"
FROM "Esprit" OR "Social" OR "Tech" OR "Langues"
WHERE startswith(file.name, "Concept-")
GROUP BY fiabilite
SORT length(rows) DESC
```

### 🔗 Connexions
* [[Guide-Conventions]] — *les règles que ce tableau contrôle.*
* [[Ref-Bibliothèque]] — *les niveaux que lit le script.*
