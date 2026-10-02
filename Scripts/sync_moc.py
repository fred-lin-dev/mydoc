#!/usr/bin/env python3
"""Aligne les données DÉRIVÉES des MOC sur les notes — emoji de verdict et compteurs.

    python3 Scripts/sync_moc.py

Ne touche **ni** les glosses, **ni** les sections, **ni** l'ordre : seulement ce que
`audit.py` vérifie déjà. Le MOC reste tenu à la main pour tout ce qui a du sens ; ce
script ne fait que la part mécanique, celle où l'erreur d'arithmétique est garantie.

Écrit après trois dérives trouvées à la main — compteurs périmés, `Corps/` absent des
requêtes Dataview, 8 notes jamais listées dans `MOC-Social`.
"""

import pathlib
import re
from collections import Counter

RACINE = pathlib.Path(__file__).resolve().parent.parent
DOMAINES = ("Esprit", "Social", "Tech", "Corps", "Langues")
LIBELLE = {"🟢": "solide", "🟠": "contesté", "🔴": "réfuté",
           "⬜": "non applicable", "⚪": "non évalué", "🔵": "invérifiable"}
LIGNE = re.compile(r"^\* ([🟢🟠🔴⚪⬜🔵]) \[\[(Concept-[^\]]+)\]\]", re.MULTILINE)
VERDICT = re.compile(r"^fiabilite: (.)", re.MULTILINE)


def main():
    touches = 0
    for domaine in DOMAINES:
        moc = RACINE / domaine / f"MOC-{domaine}.md"
        if not moc.exists():
            continue
        reel = {f.stem: VERDICT.search(f.read_text(encoding="utf-8")).group(1)
                for f in (RACINE / domaine).glob("Concept-*.md")}
        avant = texte = moc.read_text(encoding="utf-8")
        texte = LIGNE.sub(
            lambda m: f"* {reel.get(m.group(2), m.group(1))} [[{m.group(2)}]]", texte)
        compte = Counter(reel.values())
        texte = re.sub(r"\*\*\d+ notes atomiques",
                       f"**{len(reel)} notes atomiques", texte)
        for emoji, libelle in LIBELLE.items():
            texte = re.sub(rf"^(\| {emoji} {libelle} \| )\**\d+\**",
                           lambda m, e=emoji: m.group(1) + str(compte[e]),
                           texte, flags=re.MULTILINE)
        if texte != avant:
            moc.write_text(texte, encoding="utf-8")
            touches += 1
            print(f"  {domaine} aligné · {dict(compte)}")
    print(f"{touches} MOC aligné(s)" if touches else "rien à aligner")


if __name__ == "__main__":
    main()
