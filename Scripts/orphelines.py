#!/usr/bin/env python3
"""Compare les identifiants de cartes du vault et ceux d'Anki — LECTURE SEULE.

    python3 Scripts/orphelines.py

Ne supprime jamais rien : il imprime la commande à lancer, et la décision reste
à l'utilisateur — même principe que Scripts/audit.py.

⚠️  Pourquoi ce script existe. Obsidian_to_Anki **crée et met à jour, il ne
    supprime pas.** Retirer un bloc `Q:`/`A:` d'une note, ou déplacer une idée
    d'une note à l'autre, laisse dans Anki une carte que plus aucun fichier ne
    référence : elle ne sera jamais remise à jour ni effacée, et **rien ne le
    signale**. L'audit ne peut pas le voir — il est hors réseau, et Anki n'est
    pas toujours ouvert. Ce contrôle est le seul, et il est manuel.

    À lancer après tout scan qui a retiré ou déplacé une carte.
"""

import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
DOMAINES = ("Esprit", "Social", "Tech", "Corps", "Langues")
ANKI = "http://localhost:8765"
ID = re.compile(r"<!--ID: (\d+)-->")


def ids_du_vault():
    """{identifiant: chemin de la note qui le porte}."""
    trouves = {}
    for domaine in DOMAINES:
        for f in (RACINE / domaine).glob("*.md"):
            for i in ID.findall(f.read_text(encoding="utf-8")):
                trouves[i] = f.relative_to(RACINE)
    return trouves


def anki(action, **params):
    requete = json.dumps({"action": action, "version": 6, "params": params}).encode()
    with urllib.request.urlopen(ANKI, requete, timeout=10) as r:
        reponse = json.load(r)
    if reponse.get("error"):
        sys.exit(f"Anki a refusé « {action} » : {reponse['error']}")
    return reponse["result"]


def main():
    vault = ids_du_vault()
    try:
        cotes_anki = {str(i) for i in anki("findNotes", query="tag:Obsidian_to_Anki")}
    except urllib.error.URLError:
        sys.exit("Anki ne répond pas sur localhost:8765 — l'ouvrir, avec AnkiConnect.")

    orphelines = sorted(cotes_anki - set(vault))
    manquantes = sorted(set(vault) - cotes_anki)

    print(f"vault {len(vault)} cartes · Anki {len(cotes_anki)} notes\n")

    if manquantes:
        # Un identifiant écrit à la main, ou une note supprimée dans Anki. Dans les
        # deux cas le plugin échoue en silence sur ces cartes.
        print(f"🔴 {len(manquantes)} identifiant(s) du vault absent(s) d'Anki — "
              f"le scan échouera en silence sur ces cartes :")
        for i in manquantes:
            print(f"     {i}  {vault[i]}")
        print()

    if orphelines:
        infos = anki("notesInfo", notes=[int(i) for i in orphelines])
        jamais_vues = {str(n["noteId"]) for n in infos
                       if not anki("findCards", query=f"nid:{n['noteId']} -is:new")}
        print(f"🟠 {len(orphelines)} carte(s) dans Anki que plus aucun fichier ne référence.")
        print("   Elles ne seront plus jamais mises à jour ni supprimées par le plugin.\n")
        for n in infos:
            revue = "" if str(n["noteId"]) in jamais_vues else "  ⚠️ DÉJÀ RÉVISÉE"
            print(f"     {n['noteId']}{revue}")
            print(f"       {re.sub(r'<[^>]+>', '', n['fields']['Front']['value'])[:90]}")
        print("\n   Pour les supprimer — à lancer soi-même, après lecture de la liste :")
        print("     curl -s localhost:8765 -X POST -d '"
              + json.dumps({"action": "deleteNotes", "version": 6,
                            "params": {"notes": [int(i) for i in orphelines]}}) + "'")
    if not orphelines and not manquantes:
        print("✅ les deux ensembles coïncident exactement.")


if __name__ == "__main__":
    main()
