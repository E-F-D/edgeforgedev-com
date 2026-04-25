<p align="center">
  <img src="assets/logo.png" alt="EdgeForgeDev" width="120"/>
</p>

# EdgeForgeDev

> **DevOps platform with local AI for European SMBs** · GDPR-native · Self-hostable · Open Source AGPL-3.0

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
![Status](https://img.shields.io/badge/Status-Beta-orange)
![Made in France](https://img.shields.io/badge/Made_in-France-blue)

---

## What is EdgeForgeDev?

**EdgeForgeDev** is an open-source, self-hostable platform that brings local AI to DevOps and IT operations for European SMBs (50-500 employees).

We solve **3 critical problems** for SMBs in 2026:

1. **Cloud monitoring is expensive**. Datadog at 200€+/host/month? EdgeForgeDev runs on your infrastructure for a flat fee.
2. **GDPR compliance is hard**. Send your logs to US servers? Not anymore. Our AI runs locally — your data never leaves your perimeter.
3. **AI is stuck in cloud silos**. Llama, Mistral, Qwen running on YOUR Kubernetes cluster, with full RAG on YOUR documents.

## Features

🛡️ **Local AI Models** — Ollama integration, GPU-aware (RPi to enterprise servers)
📊 **Kubernetes/Docker Monitoring** — Real-time alerts via voice, Prometheus + Grafana stack
🔍 **RAG on Internal Docs** — ChromaDB + embeddings, query your knowledge base in natural language
🎙️ **Voice Operations** — Run `kubectl scale` in plain French/English via STT/TTS
📈 **ETL Logs → Insights** — DeltaLake-powered analytics, no cloud roundtrip
🔐 **GDPR by Design** — Data stays on-premise, audit trail, compliance built-in

## Pricing

| Plan | Price | For |
|---|---|---|
| **Free** | 0€ | Test, RPi/single host, 100 req/day |
| **Starter** | 79€/month flat | SMB 1-10 employees, 5 hosts |
| **Pro** | 249€/month flat | SMB 10-50 employees, 25 hosts, full IA stack |
| **Enterprise** | from 1290€/month | SMB 50-500, custom, SSO, SLA 99.5% |

→ [Get Pro license](https://gumroad.com/edgeforgedev) | [Enterprise quote](https://edgeforgedev.com/contact)

## Quick Start (Free, RPi-friendly)

```bash
docker run -d \
  --name edgeforgedev-free \
  -p 8080:80 \
  edgeforgedev/free:latest

# Access UI at http://localhost:8080
# Default model: SmolLM-1.7B (CPU-friendly, 500MB)
```

For Pro/Enterprise install, see [docs/install.md](docs/install.md).

## Architecture

```
┌────────────────────────────────────────────────────────────┐
│                  EdgeForgeDev Platform                     │
│                                                            │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │  Voice   │  │   RAG    │  │Monitoring│  │   ETL    │   │
│  │STT/TTS   │  │ChromaDB  │  │K8s/Docker│  │DeltaLake │   │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘   │
│       │             │             │             │          │
│  ┌────┴─────────────┴─────────────┴─────────────┴─────┐   │
│  │              FastAPI Orchestrator                  │   │
│  └────────────────────────┬───────────────────────────┘   │
│                           │                                │
│  ┌────────────────────────┴───────────────────────────┐   │
│  │   Local LLM Provider Chain (Ollama → Groq → OR)    │   │
│  └────────────────────────────────────────────────────┘   │
└────────────────────────────────────────────────────────────┘
```

## Why Open Source AGPL-3.0?

We chose AGPL-3.0 (vs MIT/Apache) for one reason: **protect our community against cloud-vendor capture**. If a hyperscaler forks our code to run a competing managed service, they must publish their modifications.

For commercial use cases that AGPL doesn't fit, see our [Pro/Enterprise offerings](https://edgeforgedev.com/pricing).

## Roadmap

- [x] Project bootstrap + landing
- [ ] Free tier Docker image (Q2 2026)
- [ ] Pro tier with full RAG + Voice (Q2 2026)
- [ ] Helm chart for Kubernetes (Q2 2026)
- [ ] Marketplace skills integrations (Q3 2026)
- [ ] Enterprise SSO/SLA (Q4 2026)

## Community

- 🇫🇷 Discord (coming soon)
- 📧 Newsletter (coming soon)
- 🐦 [@EdgeForgeDev](https://x.com/EdgeForgeDev) (coming soon)

## License

[GNU Affero General Public License v3.0](LICENSE)

Copyright (c) 2026 EdgeForgeDev
