from mail_sender import send_emails


if __name__ == "__main__":
    send_emails(
        from_email="support@livestage.app",
        emails_path="./emails.txt",
        subject="What’s new on LiveStage — stability, features, and top shoots",
        email_file_path="./email_body.html"
    )
