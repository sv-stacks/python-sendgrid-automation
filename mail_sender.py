import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def send_emails(from_email, emails_path, subject, email_file_path):
    emails = load_emails(emails_path)

    for email in emails:
        print(f"sending to {email}...")

        send_email(
            from_email=from_email,
            to_email=email,
            subject=subject,
            file_path=email_file_path
        )


def send_email(from_email, to_email, subject, file_path):
    message = Mail(
        from_email=from_email,
        to_emails=to_email,
        subject=subject,
        html_content=load_html_template(file_path)
    )

    try:
        load_dotenv()
        sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(f"Status code: {response.status_code}")
        return response.status_code
    except Exception as e:
        print(f"Error sending email: {e}")
        return None


def load_emails(file_path):
    emails = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            # skip empty lines
            if not line:
                continue

            # remove markdown dash if present
            if line.startswith("- "):
                line = line[2:]

            emails.append(line)

    return emails


def load_html_template(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()
