# CV Verzender - Interactieve Demo

Deze interactieve showcase-pagina is ontwikkeld voor de sollicitatie van **Junyi Zhu** als **Python Expert / Developer** bij Sopra Steria in Groningen. Het demonstreert de naadloze integratie tussen een frontend interface en een serverless Python backend op Google Cloud Platform.

## Bestanden

- **cv-sender.html** - Interactieve portfolio-pagina (single-page) die direct communiceert met de Cloud Function API.
- **env.yaml.template** - Configuratie-sjabloon (nooit echte inloggegevens hier invullen).
- **.gitignore** - Voorkomt dat gevoelige bestanden per ongeluk naar GitHub worden gepusht.

## Installatie & Gebruik

1. Kopieer `env.yaml.template` naar `env.yaml` (alleen voor lokaal gebruik/deployment).
2. Open `cv-sender.html` in een browser om de interface te testen.
3. Gebruik de knoppen om een PDF te genereren of het dossier via e-mail te verzenden.

## Deployment Opties

### Optie 1: GitHub Pages (Aanbevolen)
1. Push deze map naar uw GitHub-repository.
2. Schakel GitHub Pages in via de repository-instellingen.
3. Toegankelijk via: `https://cislinknl.github.io/about-me/cv-sender/cv-sender.html`

### Optie 2: Firebase Hosting
```bash
firebase login
firebase init hosting
firebase deploy
```

## Veiligheidsinstructies

⚠️ **Commit NOOIT `env.yaml` met echte inloggegevens!**

Het `.gitignore` bestand is geconfigureerd om de volgende bestanden te beschermen:
- `env.yaml` (bevat API-tokens/OAuth2 credentials).
- `assets/*.pdf` (persoonlijke documenten).
- Service account bestanden.

## Functionaliteiten

- ✅ **Responsive Design**: Optimaal leesbaar op desktop, tablet en mobiel.
- ✅ **Serverless Integratie**: Directe aanroep van Python 3.11 Cloud Functions.
- ✅ **Dual-Mode**: Keuze tussen directe PDF-preview of verzending via e-mail.
- ✅ **OAuth2 Beveiliging**: Veilige e-mailverzending via de officiële Gmail API.
- ✅ **Modern UI**: Gebruik van glassmorphism en professionele lay-outs.

## Tech Stack

- **Frontend:** HTML5, CSS3 (Flexbox/Grid), JavaScript (Fetch API).
- **Backend:** Python 3.11 (GCP Cloud Functions Gen 2).
- **PDF Engine:** fpdf2 (Python).
- **Hosting:** GitHub Pages & Google Cloud.

---

*Ontwikkeld voor de Sopra Steria sollicitatie - Groningen, 2026*