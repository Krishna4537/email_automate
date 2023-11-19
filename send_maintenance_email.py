import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


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


# Example usage
recipients = ['sawhil95@gmail.com', 'rajshri0999@gmail.com', 'krishna4537@gmail.com']
sender = 'krishna.d190798@gmail.com'
message = 'Service XYZ has planned maintenance on Saturday from 14:00 till 17:00 CET'
username = 'krishna.d190798@gmail.com'  # Replace with your username
password = 'zxri sglm smlm piyc'  # Replace with your password

send_email(recipients, sender, message, username=username, password=password)
