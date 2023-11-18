import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(recipients, sender, subject, message, smtp_server, smtp_port, smtp_username, smtp_password):
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    msg['Subject'] = subject

    body = message
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(sender, recipients, msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

if __name__ == "__main__":
    # Example usage
    recipients = ["John.smith@test.com", "rodger.more@test.com"]
    sender = "no-reply-sre@test.com"
    subject = "Planned Maintenance Notification"
    message = "Service XYZ has planned maintenance on Saturday from 14:00 till 17:00 CET"
    smtp_server = "your_smtp_server"
    smtp_port = 587  # Update with your SMTP server port
    smtp_username = "your_smtp_username"
    smtp_password = "your_smtp_password"

    send_email(recipients, sender, subject, message, smtp_server, smtp_port, smtp_username, smtp_password)
