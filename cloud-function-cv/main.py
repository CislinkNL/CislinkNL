import os
import json
import base64
from email.message import EmailMessage
import functions_framework
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# --- CONFIGURATION ---
GMAIL_TOKEN_JSON_STR = os.environ.get('GMAIL_TOKEN_JSON')
PDF_FILE_PATH = 'AI_Augmented_Cloud_Architect.pdf'

def get_static_pdf():
    """Read and return the static PDF file bytes"""
    with open(PDF_FILE_PATH, 'rb') as f:
        return f.read()

class ProfessionalPDF(FPDF):
    def header(self):
        self.set_fill_color(40, 50, 70)
        self.rect(0, 0, 210, 40, 'F')
        self.set_text_color(255, 255, 255)
        self.set_font('Helvetica', 'B', 24)
        self.set_xy(10, 12)
        self.cell(0, 10, 'JUNYI ZHU', 0, 1, 'L')
        self.set_font('Helvetica', '', 14)
        self.set_xy(10, 22)
        self.cell(0, 10, 'AI-Augmented Cloud Architect | Python Expert', 0, 1, 'L')
        self.set_font('Helvetica', '', 9)
        self.set_xy(120, 12)
        self.cell(80, 5, 'Groningen, Netherlands', 0, 2, 'R')
        self.cell(80, 5, '+31 6 8888 8188', 0, 2, 'R')
        self.cell(80, 5, 'admin@cislink.nl', 0, 2, 'R')
        self.cell(80, 5, 'github.com/CislinkNL', 0, 2, 'R')
        self.ln(20)

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(128, 128, 128)
        footer_text = f'Solicitatie Dossier - Junyi Zhu - Pagina {self.page_no()}'
        self.cell(0, 10, footer_text, 0, 0, 'C')

    def section_title(self, label):
        self.set_left_margin(15) 
        self.ln(8)
        self.set_font('Helvetica', 'B', 14)
        self.set_text_color(0, 51, 102) 
        self.cell(0, 8, label.upper(), 0, 1, 'L')
        self.set_draw_color(100, 100, 100)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(4)

    def subsection_title(self, label, date=None):
        self.set_left_margin(15)
        
        # 1. Print Date FIRST (Right aligned)
        # This prevents the title from pushing the date off if the title is long
        if date:
            self.set_font('Helvetica', 'I', 10)
            self.set_text_color(100, 100, 100)
            # Save current Y
            y_pos = self.get_y()
            # Move to right side
            self.set_x(170) 
            self.cell(25, 7, date, 0, 0, 'R')
            # Restore X to left margin for title
            self.set_xy(15, y_pos)

        # 2. Print Title (Left aligned)
        self.set_font('Helvetica', 'B', 12)
        self.set_text_color(0, 0, 0)
        
        # Check if title is very long, if so, use multi_cell to wrap it safely
        # Available width for title = Page Width - Margins - Date Space
        # 210 - 15 - 15 - 30 (for date) = 150
        self.multi_cell(150, 7, label)
        
        # No extra line break needed because multi_cell moves the cursor down

    def body_text(self, text):
        self.set_left_margin(15)
        self.set_x(15)
        self.set_font('Helvetica', '', 10)
        self.set_text_color(40, 40, 40)
        self.multi_cell(175, 5, text)
        self.ln(2)

    def bullet_point(self, text):
        self.set_font('Helvetica', '', 10)
        self.set_text_color(40, 40, 40)
        self.set_left_margin(15)
        self.set_x(15)
        self.cell(5, 5, chr(149), 0, 0) 
        indent_margin = 22
        self.set_left_margin(indent_margin)
        self.set_x(indent_margin)
        self.multi_cell(165, 5, text)
        self.set_left_margin(15)

def create_pdf(cv_type='standard'):
    pdf = ProfessionalPDF()
    pdf.set_margins(15, 20, 15)
    pdf.add_page()

    if cv_type == 'fullstack':
        # Full-Stack Engineer CV (English)
        pdf.set_font('Helvetica', '', 10)
        pdf.set_text_color(40, 40, 40)

        pdf.section_title("Profile")
        pdf.body_text("Passionate Full-Stack Engineer with strong Python backend and TypeScript frontend experience. As founder of Cislink, I've built end-to-end systems from event-driven billing platforms to multi-tenant restaurant ecosystems.")

        pdf.section_title("Technical Skills")
        pdf.bullet_point("Backend: Python 3.11+ (FastAPI, Async), Go (Golang), Django (familiar)")
        pdf.bullet_point("Frontend: TypeScript, Vue 3, Nuxt 3 (SSR/SSG), React, Tailwind CSS")
        pdf.bullet_point("Databases: PostgreSQL, Firestore (NoSQL), Firebase Realtime DB")
        pdf.bullet_point("Cloud: GCP (Cloud Run, Functions, Pub/Sub), Docker, CI/CD")
        pdf.bullet_point("AI/LLM: Gemini 2.5 Native Audio, Claude 4.5, GPT-5.2, Agentic systems")

        pdf.section_title("Work Experience")
        pdf.subsection_title("Founder & Lead Architect | Cislink", "Groningen | 2023 - Present")

        pdf.bullet_point("Cloud Billing System: Event-driven Python/GCP architecture processing 50K+ EUR monthly invoices in <10 seconds")
        pdf.bullet_point("Multi-Tenant POS Ecosystem: Android POS (Kotlin) + Cloud backend + Dual-engine print server (Go+Python)")
        pdf.bullet_point("AI Voice Operator: Real-time voice AI (Gemini 2.5 + Twilio) handling phone orders")
        pdf.bullet_point("Food Delivery Platform: Startup venture, solo full-stack development for 500+ restaurants, prototype testing phase")

        pdf.section_title("Key Projects")
        pdf.bullet_point("Voice AI Demo: Call +31 970 10256688 for live conversation")
        pdf.bullet_point("Food Delivery: mealone.web.app - Full-stack Nuxt 3 application")
        pdf.bullet_point("CV Generator: This PDF is auto-generated by Python Cloud Function")

        pdf.section_title("Education")
        pdf.body_text("Self-Taught Software Engineer | Continuous Learning & Practice | 2018 - Present")
        pdf.body_text("Chose entrepreneurship over traditional education. Operate at proven HBO/WO level through successful commercial systems.")

    else:
        # Standard Dutch CV
        pdf.section_title("Profiel Samenvatting")
        pdf.body_text("AI-Augmented Full Stack Cloud Architect. Specialist in het vertalen van complexe business requirements naar robuuste cloud-native architecturen.")

        pdf.section_title("LIVE INTERACTIEVE DEMO'S")
        pdf.subsection_title("1. Voice AI Operator (Twilio & Gemini)")
        pdf.body_text("Bel naar +31 970 10256688 voor een real-time gesprek met mijn AI-agent.")

        pdf.subsection_title("2. Automatische PDF Generatie")
        pdf.body_text("Deze PDF is zojuist on-the-fly gegenereerd door een Python Cloud Function. Bekijk de broncode op mijn GitHub.")

        pdf.section_title("Kernprojecten")
        pdf.subsection_title("Cislink Cloud Facturatiesysteem", "2024")
        pdf.bullet_point("GCP Cloud Functions & Event-driven architectuur. 2 uur werk naar 10 seconden.")

        pdf.subsection_title("Multi-Tenant Food Delivery Platform", "2024")
        pdf.bullet_point("Nuxt 3 + TypeScript app voor 500+ restaurants. Stripe payments, Firebase Realtime DB.")

        pdf.subsection_title("Sushi Koi POS Ecosystem", "2023")
        pdf.bullet_point("Dual-engine architectuur (Python & Go). Offline-first Android systeem.")

        pdf.section_title("Technische Vaardigheden")
        pdf.body_text("Python 3.11 (Expert), Vue 3, Nuxt 3, TypeScript, Golang, Kotlin.")
        pdf.body_text("Google Cloud Platform, Firebase, Gemini 2.5, Claude 4.5, GPT-5.2.")

    return pdf.output()

@functions_framework.http
def send_cv(request):
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type',
    }
    if request.method == 'OPTIONS':
        return ('', 204, headers)

    # Get CV type from query parameter (default: standard)
    cv_type = request.args.get('type', 'standard')
    email = request.args.get('email')

    if request.is_json:
        request_json = request.get_json(silent=True)
        if request_json:
            if 'email' in request_json:
                email = request_json['email']
            if 'type' in request_json:
                cv_type = request_json['type']

    try:
        pdf_bytes = get_static_pdf()
        filename = 'Junyi_Zhu_CV.pdf'

        if not email:
            return (pdf_bytes, 200, {
                **headers,
                'Content-Type': 'application/pdf',
                'Content-Disposition': f'inline; filename="{filename}"'
            })

        token_info = json.loads(GMAIL_TOKEN_JSON_STR)
        creds = Credentials.from_authorized_user_info(token_info)
        service = build('gmail', 'v1', credentials=creds)

        msg = EmailMessage()
        msg['Subject'] = f"Sollicitatie Dossier: Junyi Zhu ({cv_type.title()} CV)"
        msg['From'] = 'admin@cislink.nl'
        msg['To'] = email
        msg.set_content(f"Beste,\n\nHierbij ontvangt u mijn geautomatiseerde CV ({cv_type}).\n\nMet vriendelijke groet,\nJunyi Zhu")
        msg.add_attachment(bytes(pdf_bytes), maintype='application', subtype='pdf', filename=filename)

        encoded_message = base64.urlsafe_b64encode(msg.as_bytes()).decode()
        service.users().messages().send(userId="me", body={'raw': encoded_message}).execute()

        return (f'Email successfully sent to {email}', 200, headers)

    except Exception as e:
        return (f'Error: {str(e)}', 500, headers)