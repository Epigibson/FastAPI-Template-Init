from typing import Union, List
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, Personalization
from twilio.rest import Client


class NotificationService:
    @staticmethod
    def send_email_notification(recipients: List[str], subject: str, body: str) -> Union[bool, str]:
        try:
            sg = SendGridAPIClient(api_key="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")
            message = Mail(from_email="ricardo.minor@aiscs.com.mx", subject=subject)

            for recipient in recipients:
                # Personalización del destinatario
                personalization = Personalization()
                personalization.add_to(Email(recipient))
                message.add_personalization(personalization)

                # Plantilla de correo electrónico
                message.template_id = "d-545c86806c2f4e5e8291878e868bd32c"

                # Variables de sustitución
                message.dynamic_template_data = {
                    "body": body
                }

            sg.send(message)
            return True
        except Exception as e:
            return str(e)

    @staticmethod
    def send_whatsapp_notification(recipients: List[str], message: str) -> Union[bool, str]:
        try:
            account_sid = 'ACb3d5dfa4372d73ef18920aa7ec5c5f26'
            auth_token = '2f471e4c4f842ea84bd88cb2ede69cfe'
            client = Client(account_sid, auth_token)
            for recipient in recipients:
                message = client.messages.create(
                    body=message,
                    from_='whatsapp:+14155238886',
                    to=f'whatsapp:{recipient}'
                )
            return True
        except Exception as e:
            return str(e)
