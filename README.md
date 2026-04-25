# EdgeForgeDev

> **Plateforme DevOps avec IA locale pour PME françaises** · RGPD natif · Auto-hébergeable · Open Source AGPL-3.0

[![License: AGPL v3](https://img.shields.io/badge/Licence-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
![Statut](https://img.shields.io/badge/Statut-Beta-orange)
![Made in France](https://img.shields.io/badge/Made_in-France-blue)

🇫🇷 Français · [🇬🇧 English](README.en.md)

---

## Présentation

**EdgeForgeDev** est une plateforme open-source et auto-hébergeable destinée aux opérations DevOps et IT des PME françaises (50-500 salariés). Elle intègre des modèles d'intelligence artificielle locaux pour le monitoring, la documentation et l'automatisation des opérations.

Trois positionnements structurels :

1. **Maîtrise des coûts d'observabilité.** Tarification au forfait fixe sur l'infrastructure du client, sans facturation à l'usage par host ou par giga-octet ingéré.
2. **Conformité RGPD native.** Les données opérationnelles ne quittent pas le périmètre du client. Aucune transmission vers des serveurs hors UE.
3. **IA locale opérationnelle.** Modèles ouverts (Llama, Mistral, Qwen) déployés sur le cluster Kubernetes du client, avec RAG sur la documentation interne.

## Fonctionnalités

- **Modèles IA locaux** — Intégration Ollama, optimisation GPU adaptative (du Raspberry Pi au serveur d'entreprise)
- **Monitoring Kubernetes / Docker** — Alertes temps réel, stack Prometheus + Grafana
- **RAG sur documents internes** — ChromaDB et embeddings, requêtes en langage naturel
- **Opérations vocales** — Commandes `kubectl` en français ou anglais via STT/TTS
- **ETL Logs vers insights** — Analyse de logs propulsée par DeltaLake
- **RGPD by design** — Données on-premise, journalisation d'audit, conformité native

## Tarifs

| Plan | Prix | Cible |
|---|---|---|
| **Gratuit** | 0 € | Tests, Raspberry Pi ou un seul host, 100 requêtes/jour |
| **Starter** | 79 €/mois forfait | TPE 1-10 salariés, 5 hosts |
| **Pro** | 249 €/mois forfait | PME 10-50 salariés, 25 hosts, stack IA complète |
| **Entreprise** | À partir de 1 290 €/mois | PME 50-500 salariés, déploiement sur mesure, SSO, SLA 99,5 % |

→ [Licence Pro](https://gumroad.com/edgeforgedev) — [Devis Entreprise](https://edgeforgedev.com/contact)

## Démarrage rapide

```bash
docker run -d \
  --name edgeforgedev-free \
  -p 8080:80 \
  edgeforgedev/free:latest
```

- Interface web : `http://localhost:8080`
- Modèle par défaut : SmolLM-1.7B (CPU uniquement, 500 Mo)

Installation Pro/Entreprise via Helm : voir [docs/install.md](docs/install.md).

## Architecture

```
┌────────────────────────────────────────────────────────────┐
│                  Plateforme EdgeForgeDev                   │
│                                                            │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │   Voix   │  │   RAG    │  │Monitoring│  │   ETL    │   │
│  │ STT/TTS  │  │ChromaDB  │  │K8s/Docker│  │DeltaLake │   │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘   │
│       │             │             │             │          │
│  ┌────┴─────────────┴─────────────┴─────────────┴─────┐   │
│  │           Orchestrateur FastAPI                    │   │
│  └────────────────────────┬───────────────────────────┘   │
│                           │                                │
│  ┌────────────────────────┴───────────────────────────┐   │
│  │  Chaîne de fournisseurs LLM (Ollama → Groq → OR)  │   │
│  └────────────────────────────────────────────────────┘   │
└────────────────────────────────────────────────────────────┘
```

## Choix de licence AGPL-3.0

L'AGPL-3.0 protège les contributions communautaires contre la capture par les hyperscalers : un acteur cloud qui forke ce code pour proposer un service managé concurrent doit publier ses modifications.

Pour les usages commerciaux non couverts par l'AGPL (intégrations propriétaires, SaaS revendu en marque blanche), voir nos [offres Pro et Entreprise](https://edgeforgedev.com/pricing).

## Roadmap

- [x] Bootstrap projet et landing
- [ ] Image Docker du tier Gratuit (T2 2026)
- [ ] Tier Pro avec RAG et voix complets (T2 2026)
- [ ] Helm chart Kubernetes (T2 2026)
- [ ] Marketplace de skills (T3 2026)
- [ ] SaaS multi-tenants (T3 2026)
- [ ] SSO et SLA Entreprise (T4 2026)

## Projet associé

[StackBusiness](https://github.com/E-F-D/stack-business-com) — CRM commercial augmenté à l'IA. Mêmes mainteneurs, même philosophie d'auto-hébergement et de conformité RGPD.

## Communauté

- Discord
- Newsletter
- X / Twitter

## Licence

[GNU Affero General Public License v3.0](LICENSE)

Copyright (c) 2026 EdgeForgeDev
