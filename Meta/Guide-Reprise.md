---
tags: [meta/guide]
---
# 🧭 Reprise — où en est ce vault

> **À lire en premier quand on reprend le travail dans une nouvelle session.**
> Cette note existe parce qu'une partie de ce qui a été appris n'est écrite **nulle part
> ailleurs** : les régularités constatées d'un livre à l'autre, les pièges techniques
> rencontrés, et les décisions prises en cours de route.
>
> État au **2026-09-28**. Construit en une session, à partir d'un vault vide.

---

## 1 · Ce qu'il faut lire, dans cet ordre

| Fichier | Ce qu'il contient |
|---|---|
| [[Guide-Conventions]] | **la constitution.** Les 12 décisions tranchées, plus l'arborescence, la langue et les plugins. Tout le reste en découle |
| [[Guide-Méthode_Zettelkasten]] | le document d'origine, apporté par Yinpi — le raisonnement derrière chaque décision |
| cette note | l'état, les constats, les pièges |
| [[Guide-Stratégie_Lecture]] | comment les trois listes de lecture s'articulent, et le filtre ⏳ |
| [[Guide-Anki_Workflow]] | la synchronisation des cartes, et ses trois pièges |
| [[MOC-Audit]] | le tableau de bord Dataview · et `python3 Scripts/audit.py` pour le reste |

**Les quatre index par domaine :** [[MOC-Esprit]] · [[MOC-Social]] · [[MOC-Tech]] · [[MOC-Corps]].

---

## 2 · L'état, en chiffres

```
184 notes · 122 Concept- · 36 Source- · 13 Ref- · 5 MOC- · 5 Guide-
0 erreur · 0 alerte · 45 dettes ⚪ (37 de vérification + 8 fiches à écrire)
350 cartes, toutes synchronisées vers Anki
57 PDF, tous avec un niveau de périmètre
```

| Domaine | `Concept-` | `Source-` | `Ref-` |
|---|---|---|---|
| `Esprit/` | 75 | 22 | 6 |
| `Social/` | 38 | 11 | 6 |
| `Corps/` | 5 | 1 | 0 |
| `Tech/` | 4 | 2 | 0 |
| `Langues/` | **0** | 0 | 0 |

**Verdicts de fiabilité :** ⬜ 43 · ⚪ 37 · 🟠 21 · 🟢 16 · 🔴 5
**Inventaire :** 84 titres, 60 sur le disque — 37 fichés · 10 lu-sans-fiche · 19 illustration · 18 dehors
**19 titres du disque ne sont sur aucune liste de lecture**, dont 8 fichés sans fiche

---

## 3 · Ce qui a été fait

**Les 34 titres de [[Ref-Lecture_Ordre_de_Priorité]] sont traités**, en cinq phases :
Moteur, Véhicule, Navigation, Stratégie, Socle. Plus **7 romans** au niveau `illustration` —
les quatre dystopies du contrôle, deux tomes de *Fondation*, *I, Robot*.

Il ne reste **aucun livre à lire** dans les listes. La seule file de travail est celle des
37 dettes de vérification.

### Ce qui a changé par rapport au guide d'origine

Quatre ajouts au modèle, tous décidés en cours de route et consignés dans les conventions :

| Ajout | Pourquoi |
|---|---|
| **5ᵉ valeur au barème : `⬜ non applicable`** | 43 notes n'affirment rien d'empirique — définitions, préceptes, formalismes. Sans cette valeur elles seraient coincées en `⚪` et pollueraient la file de dettes |
| **4ᵉ niveau de périmètre : `illustration`** | la fiction lue pour sa structure n'est ni un manuel ni du loisir. **Règle associée : une fiction ne crée jamais de `Concept-`** — elle est citée comme exemple depuis une note existante |
| **Règle des 3 cartes** (décision 01) | le signal de découpe est mécanisable par `grep -c '^Q:'`, donc gratuit |
| **`corps/`** | né à la règle des 5, sans qu'on ait eu à décider. Premier test réel de cette règle |
| **Règle d'autonomie des cartes** (décision 08) | ajoutée le 2026-09-28 après usage réel : 92 cartes sur 350 étaient irrésolubles en révision. Une question doit nommer son sujet ; préfixe `**Titre** — ` là où elle ne se suffit pas |
| **Inventaire unique des livres** | 2026-09-29 : `Ref-Périmètre_Bibliothèque` est devenu l'inventaire complet — 84 titres, possédés ou non, avec niveau, domaine et liste d'origine. Les `Ref-Lecture_*` ont perdu leurs colonnes Domaine et Périmètre : un niveau n'est déclaré qu'à un endroit |

---

## 4 · Les cinq constats qui n'existent nulle part ailleurs

C'est la partie de cette note qui ne peut pas être reconstituée à partir du vault.

### 4.1 · Garder le geste, jeter le mécanisme — **cinq fois**

Le mode de défaillance dominant de ce corpus. Une pratique utile arrive accompagnée d'une
explication fausse, et la pratique survit à la réfutation de l'explication.

| Mécanisme réfuté ou contesté | Ce qui survit |
|---|---|
| [[Concept-Volonté_Comme_Ressource]] 🔴 — *ego depletion* | réduire le nombre de décisions reste utile |
| [[Concept-Posture_De_Pouvoir]] 🔴 — effets hormonaux | être physiquement à l'aise change ce qu'on fait de son attention |
| [[Concept-Cerveau_Triunique]] 🔴 — modèle de MacLean | certaines réactions corporelles sont peu contrôlables |
| [[Concept-Ombre_Et_Traits_Refoulés]] 🟠 — appareil jungien | une réaction disproportionnée mérite un examen |
| [[Concept-EMDR_Mécanisme_Et_Effet]] 🟠 — mouvements oculaires | la thérapie fonctionne, par exposition |

**Conséquence de méthode :** devant toute prescription appuyée sur un mécanisme, vérifier les
deux séparément. L'une peut tenir sans l'autre.

### 4.2 · L'ego depletion a contaminé **trois** livres de la liste

Ahrens, Newport et Kahneman s'y appuient. Clear la contourne, et c'est pourquoi sa
prescription survit mieux. **Un prix Nobel écrivant sur la fragilité du jugement a repris sans
réserve une littérature qui n'a pas tenu** — ce n'est pas une faute individuelle, c'est la
norme de l'époque, et c'est la meilleure justification du champ `fiabilite`.

### 4.3 · Le taux de survie a suivi exactement le calibrage annoncé

Le guide d'origine annonçait « un tiers seulement des concepts vérifiés survit intact ».

| Après la phase | Notes intactes / évaluées |
|---|---|
| 1 — Moteur | 47 % |
| 2 — Véhicule | 37 % |
| 3 — Navigation | 31 % |
| 4 — Stratégie | 27 % |
| 5 — Socle | **38 %** |

La remontée finale n'est pas un hasard : la phase 5 repose sur des **théorèmes** et de
l'épidémiologie, pas sur de la psychologie sociale de laboratoire. Et `social/` n'a
**qu'une seule note 🟢 sur 38**, contre 3 `🔴` sur les 5 du vault.

### 4.4 · Une seule critique, appliquée six fois

[[Concept-Preuve_Silencieuse]] est le défaut structurel de **six livres** : les portraits de
Newport, les cas de Voss, les anecdotes de Greene ×2, les réussites de Manson, le témoignage
de Frankl. J'ai écrit la même remarque six fois avant que la note existe — il a fallu attendre
le 23ᵉ livre. **C'est exactement ce qu'un Zettelkasten est censé produire, et ça montre aussi
sa lenteur.**

### 4.5 · Les meilleures notes ne viennent pas des livres les plus récents

Les 16 notes tirées des cinq textes primaires — Sun Tzu, Machiavel, Clausewitz, Marc Aurèle,
Nietzsche — sont presque toutes `⬜`, et **les plus citées du vault**. Elles sont abstraites,
donc portables. Symétriquement, les meilleures notes techniques ne parlent pas de code :
[[Concept-Orthogonalité]] justifie la décision 03, [[Concept-DRY]] la source unique du
périmètre, [[Concept-Fenêtre_Brisée]] l'existence de l'audit.

---

## 5 · Les pièges techniques rencontrés, et leurs corrections

| Piège | Ce qui s'est passé | Correction |
|---|---|---|
| **Le plugin écrase sa config** | l'ajout de `Corps` à `FOLDER_DECKS`, fait sur le disque pendant qu'Obsidian tournait, a disparu au scan suivant | **toujours passer par le panneau de réglages du plugin.** Contrôle ajouté à l'audit ; documenté dans [[Guide-Anki_Workflow]] |
| **Un scan sans couche de texte** | `The_48_Laws_of_Power.pdf` n'avait aucun texte extractible | océrisé, 476 pages, qualité mesurée à **0,060 %** d'anomalies. Nécessite `tesseract-data-eng` |
| **Un niveau absent du script** | `illustration` ajouté au modèle mais pas à la liste reconnue par `audit.py` — il ignorait silencieusement ces lignes | corrigé. **C'est l'angle mort annoncé par la décision 09 : vérifier le script lui aussi** |
| **Un filigrane injecté** | `Why_We_Sleep.pdf` porte une URL **381 fois**, une par page, au milieu du texte | filtrer à l'extraction, sinon il entre dans les citations |
| **Un lien de catégorie impossible** | j'ai écrit `[[Source-Beyond_Good_and_Evil]]` pour un livre `lu-sans-fiche`, qui n'aura jamais de fiche | l'audit l'a détecté. Les notes de ces livres pointent le **PDF** |
| **Noms de fichiers non conformes** | 12 PDF arrivés avec espaces, tirets, casse basse, slugs d'URL | renommés. **Déplacer un PDF ne casse rien, le renommer casse la fiche qui le cite** |
| **Cartes écrites la note sous les yeux** | 92 questions sur 350 renvoyaient à « ce principe », « cette règle », « le livre » — lisibles à l'écriture, illisibles en révision, où Anki tire dans le désordre | préfixe `**Titre** — `, règle inscrite en décision 08, contrôle ajouté à l'audit. **Le défaut est invisible au rédacteur par construction** : c'est le seul du lot qu'aucune relecture de la note ne révèle |
| **Une duplication qui avait commencé à divarier** | le domaine et le niveau de chaque livre vivaient dans deux fichiers. Pas encore de divergence sur les niveaux, mais déjà sur les noms : *De la guerre* dans la liste, `On_War` au périmètre — donc irréconciliable par script | inventaire unique, et les listes n'en parlent plus. **Le signal d'alarme n'était pas une erreur mais un nom qui ne s'apparie pas** |
| **Un garde-fou borgne** | le garde-fou 11 vérifiait qu'une fiche produit une note, jamais qu'un livre fiché a une fiche. **Huit livres attendaient en silence**, six depuis la construction du vault | contrôle ajouté, comptés en dette. Un garde-fou qui ne teste qu'un sens laisse passer l'autre |

---

## 6 · Ce qui reste à faire

### La seule file de travail : 37 dettes `⚪ non évalué`

À 20 min – 1 h par concept, c'est **12 à 37 heures**. À payer **par ordre d'utilité**, jamais
d'arrivée : le premier tableau de [[MOC-Audit]] les trie par nombre de liens entrants.

Les plus rentables sont celles qui servent de prémisse à d'autres —
[[Concept-Dépendance_Au_Regard]], [[Concept-Polarisation]],
[[Concept-Vulnérabilité_Comme_Signal]] portent chacune trois notes de séduction.

**19 des 37 sont dans `social/`**, le domaine le plus fragile : coût le plus élevé, rendement
attendu le plus faible.

### Trous connus

- **`Langues/` est vide.** `English_Phrasal_Verbs` est `lu-sans-fiche`, et la décision 02b a
  écarté un préfixe `Vocab-`. ⚠️ **À rouvrir avant d'attaquer le vocabulaire :** l'ancien vault
  avait un type de note Anki `Vocabulaire_Elite` avec un champ *Exemple*, conservé dans la
  configuration du plugin et inutilisé.
- **Une note manquante que rien ne peut combler par la fiction :** la **spécification
  incomplète**, qu'illustre parfaitement *I, Robot* — mais une fiction ne crée pas de
  `Concept-`. Elle devra venir de littérature technique. Voir [[Source-I_Robot]].
- **`Ref-Lecture_SciFi_Stratégique`** : 11 romans sur 18 pas encore acquis.
- **Deux déplacements de lecture recommandés et non appliqués** dans
  [[Ref-Lecture_Ordre_de_Priorité]] : *Thinking, Fast and Slow* en phase 1, *Thinking in
  Systems* en phase 4.

### Une contradiction assumée, à ne pas « corriger »

[[Concept-Terrain_De_Mort]] dit de supprimer ses options ; [[Concept-Surface_D_Exposition]] et
[[Concept-Optionalité]] disent de les garder. **Le critère de partage est écrit dans la
première note** — supprimer si le problème est l'exécution, garder si c'est l'information.
C'est la seule contradiction explicite du vault, et elle est plus informative que si elle
avait été tranchée.

---

## 7 · Réflexes à conserver

1. **Lancer `python3 Scripts/audit.py` avant et après chaque séance.** Il ne modifie rien.
2. **Jamais de `mv` ni de `rm` sur un `.md`** — F2 ou glisser-déposer dans Obsidian, décision 10.
3. **Ne jamais écrire un identifiant de carte à la main.** Échec silencieux garanti.
4. **Vérifier dans le PDF avant d'écrire.** Sur 36 livres, six étaient en traduction sans que
   rien ne l'annonce, un était un scan, un portait un filigrane, et *Propaganda* s'est révélé
   français alors que je le cherchais en anglais.
5. **Une fiction ne crée jamais de `Concept-`.**
6. **Quand une règle produit surtout des faux positifs, corriger la règle** — pas les notes.

### 🔗 Connexions
* [[Guide-Conventions]] — *les 12 décisions, et tout ce qui en découle.*
* [[Guide-Méthode_Zettelkasten]] — *le raisonnement d'origine.*
* [[MOC-Audit]] — *l'état réel, en direct.*
