import requests
from decouple import config
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from mailjet_rest import Client

# Mailjet client setup
MAILJET_API_KEY = config("MAIL_JET_PUBLIC_KEY")
MAILJET_API_SECRET = config("MAIL_JET_SECRET_KEY")
mailjet = Client(auth=(MAILJET_API_KEY, MAILJET_API_SECRET), version="v3.1")


class EmailService:

    def __init__(self, from_email, to_email, to_name):
        self.from_email = from_email
        self.to_email = to_email
        self.to_name = to_name

    def send_email(self, subject, template_name, context):
        """Sends an email with the given subject, template, and context."""
        html_content = self._render_email_html(template_name, context)

        data = {
            "Messages": [
                {
                    "From": {
                        "Email": self.from_email,
                        "Name": "Humanitarian Logistics",
                    },
                    "To": [
                        {
                            "Email": self.to_email,
                            "Name": self.to_name,
                        },
                    ],
                    "Subject": subject,
                    "TextPart": strip_tags(html_content),
                    "HTMLPart": html_content,
                }
            ]
        }

        self._send_via_mailjet(data)

    def _render_email_html(self, template_name, context):
        """Renders the email template with the given context."""
        return render_to_string(template_name=template_name, context=context)

    def _send_via_mailjet(self, data):
        """Sends an email via Mailjet with the given data."""
        try:
            response = mailjet.send.create(data=data)
            if response.status_code != 200:
                raise Exception(f"Mailjet API error: {response.json()}")
        except Exception as e:
            print(f"Failed to send email: {e}")
