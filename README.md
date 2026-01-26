# Hi there, I'm Junyi Zhu 👋

## AI-Augmented Cloud Architect | Python Specialist | SaaS Founder

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Google Cloud](https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)](https://cloud.google.com/)
[![Firebase](https://img.shields.io/badge/Firebase-FFCA28?style=for-the-badge&logo=firebase&logoColor=black)](https://firebase.google.com/)
[![Kotlin](https://img.shields.io/badge/Kotlin-7F52FF?style=for-the-badge&logo=kotlin&logoColor=white)](https://kotlinlang.org/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com/)
[![Gemini](https://img.shields.io/badge/Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/)
[![Claude](https://img.shields.io/badge/Claude-CC9966?style=for-the-badge&logo=anthropic&logoColor=white)](https://www.anthropic.com/)

📍 **Groningen, The Netherlands** | 🤝 **Open to Hybrid/On-site** | 📧 admin@cislink.nl

---

## 🎯 The Hybrid Architect

> **I bridge the gap between Enterprise Stability and AI Innovation.**

Leveraging advanced AI workflows (Gemini/Claude) to deliver production-grade systems with **3x efficiency**.

I build scalable cloud-native solutions that combine:
- **Enterprise-grade reliability** — Event-driven architectures, zero-downtime deployments
- **AI-first development** — LLM-powered agents, real-time voice AI, intelligent automation
- **Full-stack delivery** — From bare metal (IoT/Android) to serverless backends

---

## 🏆 Featured Projects

| Project | Stack | Impact |
|:--------|:------|:-------|
| **🧾 [Cislink Cloud Invoice Engine](https://github.com/CislinkNL)** | ![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square) ![GCP](https://img.shields.io/badge/GCP-Functions_2nd_Gen-4285F4?style=flat-square&logo=google-cloud) ![Pub/Sub](https://img.shields.io/badge/Pub--Sub-yellow-700?style=flat-square) | **Event-driven architecture** automating billing for 1000+ clients. Zero-maintenance serverless design. Processes €50K+ monthly invoices; reduced processing time from 2 hours → 10 seconds. |
| **🤖 [Real-time AI Voice Operator](https://github.com/CislinkNL/voice-ai-python)** | ![Python](https://img.shields.io/badge/Python-3.12-blue?style=flat-square) ![Gemini](https://img.shields.io/badge/Gemini_Live_API-4285F4?style=flat-square&logo=google) ![Twilio](https://img.shields.io/badge/Twilio-F22F46?style=flat-square) | **Autonomous voice agent** handling restaurant reservations via phone. Replaces traditional IVR with GenAI. Deployed on Google Cloud Run; sends WhatsApp confirmations. |
| **📱 Multi-Tenant POS Ecosystem** | ![Kotlin](https://img.shields.io/badge/Kotlin-Android-7F52FF?style=flat-square) ![Firebase](https://img.shields.io/badge/Firebase-FFCA28?style=flat-square&logo=firebase) ![IoT](https://img.shields.io/badge/IoT-ESC/POS-00979D?style=flat-square) | **End-to-end restaurant platform**: Android POS + Cloud backend + Kitchen printers. Dual-engine (Go+Python) print server for 100% uptime. |

---

## 🛠️ Technical Arsenal

### Cloud & Backend
- **Languages:** Python (3.11+), Go (Golang), Kotlin, TypeScript
- **Cloud Platforms:** Google Cloud Platform (Cloud Run, Cloud Functions, Pub/Sub, Firestore)
- **Architecture:** Event-driven, Serverless, Microservices
- **Databases:** Firestore (NoSQL), PostgreSQL, Firebase Realtime Database

### AI & LLMs
- **Models:** Gemini 2.5 (Live API), Claude, GPT-4
- **Applications:** Real-time voice AI, Function Calling, RAG systems, Multi-agent workflows
- **Integration:** WebRTC, WebSocket, Twilio Media Streams

### DevOps & Infrastructure
- **Containerization:** Docker, Cloud Run
- **CI/CD:** GitHub Actions, Cloud Build
- **Monitoring:** Cloud Logging, Cloud Monitoring
- **Hardware:** ESC/POS thermal printers, Android devices

---

## 🚀 Live Demo: AI-Augmented Automation

Experience my Python & Cloud automation in action:

[![Live Demo](https://img.shields.io/badge/DEMO-Interactive_CV_Generator-red?style=for-the-badge&logo=google-cloud&logoColor=white)](https://cislinknl.github.io/about-me/cv-sender/cv-sender.html)

**What happens behind the scenes:**
1. Frontend (GitHub Pages) captures your request
2. GCP Cloud Function (Python 3.11) generates a professional PDF on-the-fly
3. Gmail API (OAuth2) delivers it securely

**Tech Stack:** Python 3.11 · GCP Cloud Functions (Gen 2) · fpdf2 · GitHub Pages

---

## 📈 Architectural Preview

Event-driven architecture I designed for scalability and fault tolerance:

```mermaid
graph TD
    subgraph Clients
        Web[Web Dashboard]
        POS[Android POS]
    end

    subgraph "GCP Serverless"
        API[API Gateway / Cloud Functions]
        Auth[Firebase Auth]

        subgraph "Async Processing"
            PubSub{Pub/Sub}
            Worker[Invoice Generator]
        end

        DB[(Firestore)]
        Storage[(Cloud Storage)]
    end

    Web -->|HTTPS| API
    POS -->|HTTPS| API
    API -->|Trigger| PubSub
    PubSub -->|Push| Worker
    Worker -->|Read/Write| DB
    Worker -->|Store| Storage

    style Worker fill:#4285F4,stroke:#fff,color:#fff
    style PubSub fill:#FBBC05,stroke:#fff,color:#333
    style DB fill:#EA4335,stroke:#fff,color:#fff
```

---

## 💼 Why I'm the Right Match

- **📍 Local to Groningen** — Immediately available, no relocation needed
- **🗣️ Native Dutch** — Fluent in the language of the workplace and clients
- **☁️ Cloud-Native Expertise** — Deep experience with Python 3.11+, GCP, event-driven architectures
- **🤖 AI-Driven Workflow** — 3-5x productivity boost through strategic AI (Gemini/Claude) integration
- **🚀 Entrepreneurial DNA** — Solo-founder of multi-tenant SaaS platforms (Cislink)
- **🔧 Full-Stack Delivery** — From cloud infra & Python backends to Android (Kotlin)

---

## 📬 Get In Touch

- **📧 Email:** [admin@cislink.nl](mailto:admin@cislink.nl)
- **📱 Phone:** [+31 6 8888 8188](tel:+31688888188)
- **🔗 GitHub:** [github.com/CislinkNL](https://github.com/CislinkNL)
- **🌐 Website:** [cislink.nl](https://cislink.nl)

---

*Built with ⚡ by an AI-augmented developer in Groningen, Netherlands*
