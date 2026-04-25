#!/usr/bin/env python3
"""
Fetch 100 PME tech IDF prospects via API recherche-entreprises gouv.fr (open data, gratuit).

Usage:
    python3 fetch_prospects_idf.py > prospects_idf.csv

Cible:
- PME tech IDF 50-499 salariés
- NAF 62.01Z (Programmation), 62.02A (Conseil info), 62.02B (Tierce maintenance),
  62.03Z (Gestion installations info), 62.09Z (Autres activités info),
  63.11Z (Traitement données/hébergement)
- Départements 75, 77, 78, 91, 92, 93, 94, 95

Sortie CSV avec colonnes adaptées au modèle SB CRM Lead.
"""

import csv
import sys
import time
import urllib.request
import urllib.parse
import json

# Configuration
API_BASE = "https://recherche-entreprises.api.gouv.fr/search"
NAF_TECH = ["62.01Z", "62.02A", "62.02B", "62.03Z", "62.09Z", "63.11Z"]
DEPTS_IDF = ["75", "77", "78", "91", "92", "93", "94", "95"]
TRANCHES = ["41", "42", "51", "52"]  # 50-99, 100-199, 200-249, 250-499 salariés
TARGET_COUNT = 100
PER_PAGE = 25

# Mapping tranche effectif INSEE → label lisible
TRANCHE_LABEL = {
    "41": "50-99 sal.",
    "42": "100-199 sal.",
    "51": "200-249 sal.",
    "52": "250-499 sal.",
}


def fetch_page(naf, page=1):
    """Fetch une page de résultats pour un NAF donné."""
    params = {
        "activite_principale": naf,
        "tranche_effectif_salarie": ",".join(TRANCHES),
        "page": page,
        "per_page": PER_PAGE,
        "etat_administratif": "A",  # uniquement entreprises actives
    }
    url = f"{API_BASE}?{urllib.parse.urlencode(params)}"
    try:
        with urllib.request.urlopen(url, timeout=10) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print(f"# WARN: fetch error {naf} page {page}: {e}", file=sys.stderr)
        return {"results": [], "total_pages": 0}


def is_idf(siege):
    """Vérifie que le siège est en IDF (département 75, 77, 78, 91, 92, 93, 94, 95)."""
    if not siege:
        return False
    code_postal = siege.get("code_postal", "")
    if not code_postal:
        return False
    return code_postal[:2] in DEPTS_IDF


def main():
    prospects = []
    seen_sirens = set()

    print(f"# Recherche {TARGET_COUNT} prospects PME tech IDF 50-499 sal.", file=sys.stderr)
    print(f"# NAF: {NAF_TECH}", file=sys.stderr)
    print(f"# Tranches: {TRANCHES}", file=sys.stderr)
    print(f"# Départements: {DEPTS_IDF}", file=sys.stderr)

    # Récupère les résultats pour chaque NAF
    for naf in NAF_TECH:
        page = 1
        while len(prospects) < TARGET_COUNT:
            data = fetch_page(naf, page=page)
            results = data.get("results", [])
            if not results:
                break

            for e in results:
                siren = e.get("siren", "")
                if siren in seen_sirens:
                    continue

                siege = e.get("siege", {})
                if not is_idf(siege):
                    continue

                seen_sirens.add(siren)

                # Dirigeants (premier listé en général)
                dirigeants = e.get("dirigeants", [])
                dirigeant_principal = ""
                if dirigeants:
                    d = dirigeants[0]
                    nom_complet = d.get("nom_complet")
                    if nom_complet:
                        dirigeant_principal = nom_complet
                    else:
                        prenom = d.get("prenoms", "")
                        nom = d.get("nom", "")
                        dirigeant_principal = f"{prenom} {nom}".strip()

                prospect = {
                    "siren": siren,
                    "company_name": e.get("nom_complet", ""),
                    "contact_name": dirigeant_principal,
                    "naf_code": e.get("activite_principale", ""),
                    "naf_label": e.get("section_activite_principale", ""),
                    "city": siege.get("libelle_commune", ""),
                    "postal_code": siege.get("code_postal", ""),
                    "department": siege.get("code_postal", "")[:2] if siege.get("code_postal") else "",
                    "address": siege.get("adresse", ""),
                    "tranche_effectif": TRANCHE_LABEL.get(e.get("tranche_effectif_salarie", ""), ""),
                    "annee_effectif": e.get("annee_effectifs", ""),
                    "date_creation": e.get("date_creation", ""),
                    "categorie_entreprise": e.get("categorie_entreprise", ""),
                    "source_csv": "annuaire-entreprises-gouv-fr",
                    "tags": "source:gouv-api,priority:medium,product:edf,product:sb",
                }
                prospects.append(prospect)

                if len(prospects) >= TARGET_COUNT:
                    break

            if page >= data.get("total_pages", 0):
                break
            page += 1
            time.sleep(0.3)  # politesse rate-limit

        if len(prospects) >= TARGET_COUNT:
            break

    print(f"# Récupéré {len(prospects)} prospects uniques IDF", file=sys.stderr)

    # Sortie CSV stdout
    if prospects:
        writer = csv.DictWriter(sys.stdout, fieldnames=prospects[0].keys())
        writer.writeheader()
        writer.writerows(prospects)


if __name__ == "__main__":
    main()
