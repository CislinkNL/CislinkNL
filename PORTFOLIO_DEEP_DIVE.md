# Portfolio Deep Dive: Engineering voor Schaalbaarheid
**Auteur:** Junyi Zhu

Dit document biedt een technische diepgang in de architecturale beslissingen die zijn genomen tijdens de ontwikkeling van het Cislink-ecosysteem. Deze projecten demonstreren mijn vermogen om complexe, cloud-native systemen te ontwerpen en te implementeren met een focus op schaalbaarheid, betrouwbaarheid en automatisering.

---

## 1. Multi-Tenant Architectuur (Cislink SaaS)

### De Uitdaging
Het bouwen van een SaaS-platform voor 500+ restaurants vereist een datamodel dat volledige isolatie tussen klanten garandeert, terwijl snelle, wereldwijde updates mogelijk blijven.

### De Oplossing: Configuratie-Gedreven Ontwerp
Ik heb een hiërarchische multi-tenant structuur ontworpen in Google Firestore die elk restaurant als een geïsoleerde entiteit behandelt.

*   **Data Isolatie:** Alle restaurantgegevens (menu's, bestellingen, statistieken) zijn genest onder een unieke `rest_[6-cijferige]` ID. Dit voorkomt datalekken en zorgt ervoor dat query-prestaties constant blijven, zelfs als het platform groeit.
*   **Branding via Configuratie:** In plaats van UI-elementen hard te coderen, haalt het systeem een JSON-configuratie op per restaurant. Dit maakt onmiddellijke updates van logo's, kleuren en functionaliteiten mogelijk op alle platforms (Web/Android) zonder code opnieuw te implementeren.
*   **Schaalbaarheidspad:** De architectuur is ontworpen aan de hand van een "Fase 1 naar Fase 3" roadmap, waardoor de overgang van 5 naar 500+ locaties geen structurele refactoring vereist.

---

## 2. Event-Driven Facturatie (Python/GCP)

### De Uitdaging
Het genereren van high-fidelity PDF-facturen voor zakelijke catering kan rekenintensief zijn. Synchrone generatie leidt vaak tot time-out problemen en een slechte gebruikerservaring.

### De Oplossing: Serverless Worker Pattern
Ik heb een asynchrone, event-driven pipeline geïmplementeerd met **GCP Cloud Functions (Gen 2)** en **Pub/Sub**.

*   **Ontkoppeling:** Wanneer een gebruiker een factuur aanvraagt, bevestigt de API de aanvraag onmiddellijk en publiceert een bericht naar een Pub/Sub-topic.
*   **Betrouwbare Verwerking:** Een specifieke Python-worker (Cloud Function) luistert naar het topic. Als de generatie faalt (bijv. door een tijdelijke API time-out), treedt de retry-logica van Pub/Sub in werking.
*   **Idempotentie:** Ik heb een mechanisme geïmplementeerd om te garanderen dat retries niet leiden tot dubbele factuurnummers of dubbele kosten—een cruciale vereiste voor de Nederlandse BTW-wetgeving.

---

## 3. Real-Time AI Voice Operator (Gemini Live)

### De Uitdaging
Het verwerken van natuurlijke spraak in een rumoerige horeca-omgeving met een latentie die laag genoeg is (<500ms) om als een echt gesprek aan te voelen.

### De Oplossing: Async Python & WebRTC
*   **Concurrency:** Gebruik van Python's `asyncio` om gelijktijdige audiostreams en API-aanroepen af te handelen.
*   **Lage Latentie:** Inzet van WebRTC voor audiotransport om de overhead van traditionele HTTP-verzoeken te omzeilen.
*   **Context Management:** Gebruik van een state machine om de "Bestellingscontext" bij te houden (bijv. "Klant heeft een burger toegevoegd," "Vraagt nu naar drankjes"), waardoor de AI gedurende het hele gesprek de focus behoudt.

---

## 4. Dual-Engine Architectuur: Python & Go (Sushi Koi)

### De Uitdaging
De "Bonserver" (keuken-printserver) is een kritiek onderdeel van de infrastructuur. Het moet real-time bestelstromen, lokale hardware-communicatie (USB/Netwerk printers) en remote monitoring afhandelen met 100% betrouwbaarheid.

### De Oplossing: Migratie van Python naar Go
Ik heb een "dual-engine" roadmap beheerd waarbij ik het systeem initieel in Python bouwde voor snelle prototyping en later de performance-kritieke componenten naar Go migreerde.

*   **Python Engine:** Gebruikt voor complexe bedrijfslogica, SKU-vertalingen en integratie met het beheerdersdashboard. De flexibiliteit maakte snelle iteratie van functies mogelijk.
*   **Go Engine (Bonserver-Go):** Herschreven in Golang om gebruik te maken van het superieure concurrency-model (Goroutines) en geheugenefficiëntie. Dit garandeert dat hardware-communicatie stabiel blijft, zelfs tijdens piekuren (100+ bestellingen per minuut).
*   **Hardware Integratie:** Diepe integratie met ESC/POS thermische printers, inclusief custom diagnostische systemen om communicatiefouten te detecteren en automatisch te herstellen.

---

## 5. Offline-First POS (Kotlin/Android)

### De Uitdaging
Restaurants kunnen niet stoppen met werken als het internet uitvalt. De POS moet volledig functioneel blijven en uiteindelijk consistent zijn met de cloud.

### De Oplossing: Reactieve Data Sync
*   **Local-First:** Gebouwd met Kotlin Coroutines en Room (SQLite) voor lokale opslag. Alle UI-interacties verlopen eerst via de lokale database.
*   **Conflictresolutie:** Wanneer de verbinding is hersteld, gebruikt een synchronisatieservice op de achtergrond een "timestamp-based win" logica om conflicten tussen meerdere POS-terminals op te lossen.

---

## 6. Automatisering: De AI-Geaugmenteerde Workflow

Als solo-ontwikkelaar zet ik AI niet alleen in voor code, maar ook voor **Architecturale Validatie**.

*   **Prompt Engineering:** Ik gebruik gestructureerde prompts om unit-tests te genereren voor complexe edge-cases in BTW-berekeningen.
*   **Documentation as Code:** Ik beheer architectuurspecificaties die fungeren als de "Source of Truth" voor zowel mijzelf als mijn AI-ontwikkelagents.
*   **Efficiëntie:** Deze workflow stelt mij in staat om systemen te bouwen die normaal gesproken een team van 4 personen (Backend, Frontend, Android, DevOps) zouden vereisen.