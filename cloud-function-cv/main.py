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

@functions_framework.http
def send_cv(request):
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type',
    }
    if request.method == 'OPTIONS':
        return ('', 204, headers)

    email = request.args.get('email')

    if request.is_json:
        request_json = request.get_json(silent=True)
        if request_json and 'email' in request_json:
            email = request_json['email']

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
        msg['Subject'] = "Sollicitatie Dossier: Junyi Zhu (CV)"
        msg['From'] = 'admin@cislink.nl'
        msg['To'] = email
        msg.set_content("Beste,\n\nHierbij ontvangt u mijn CV.\n\nMet vriendelijke groet,\nJunyi Zhu")
        msg.add_attachment(pdf_bytes, maintype='application', subtype='pdf', filename=filename)

        encoded_message = base64.urlsafe_b64encode(msg.as_bytes()).decode()
        service.users().messages().send(userId="me", body={'raw': encoded_message}).execute()

        return (f'Email successfully sent to {email}', 200, headers)

    except Exception as e:
        return (f'Error: {str(e)}', 500, headers)
