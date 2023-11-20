import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys


def send_email(recipients,
               sender,
               message,
               server='smtp.gmail.com',
               port=587,
               username='',
               password=''):
  # Create a multipart message
  msg = MIMEMultipart()
  msg['From'] = sender
  msg['To'] = ", ".join(recipients)
  msg['Subject'] = "Weekly Maintenance Notification"

  # Attach the message to the MIMEMultipart object
  msg.attach(MIMEText(message, 'plain'))

  try:
    # Set up the SMTP server
    with smtplib.SMTP(server, port) as server:
      server.ehlo()
      server.starttls()
      server.ehlo()
      server.login(username, password)
      # Send the message
      server.sendmail(sender, recipients, msg.as_string())
      print("Email sent successfully!")
      
  except Exception as e:
    print(f"Failed to send email: {e}")


if __name__ == "__main__":
    recipients = sys.argv[1].split(',')
    sender = sys.argv[2]
    message = sys.argv[3]
    username = sys.argv[4]
    password = sys.argv[5]
    smtp_server = sys.argv[6] if len(sys.argv) > 6 else 'smtp.gmail.com'
    

    send_email(recipients, sender, message, server=smtp_server, username=username, password=password)


