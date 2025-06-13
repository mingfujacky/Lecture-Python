"""
write a python program to send email automatically.
1. cwd/restricted/assets/auto_email/list.txt store receivers' email address
2. home/secrets.json store sender's email address and password
3. email title: auto sending, do not reply
4. email body: thanks for coming Python class
"""
import smtplib
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pathlib import Path

# Load sender credentials
with open(str(Path.home() / "secrets.json"), "r") as f:
    secrets = json.load(f)
sender_email = secrets["email"]
sender_password = secrets["password"]

# Load recipient emails
list_path = Path.cwd() / "restricted" / "assets" / "auto_email" / "list.txt"
with open(list_path, "r") as f:
    recipients = [line.strip() for line in f if line.strip()]

# Email content
subject = "auto sending, do not reply"
body = "thanks for coming Python class"

# Create the email
msg = MIMEMultipart()
msg["From"] = sender_email
msg["Subject"] = subject
msg.attach(MIMEText(body, "plain"))

# Send email to each recipient
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender_email, sender_password)
    for recipient in recipients:
        msg["To"] = recipient
        server.sendmail(sender_email, recipient, msg.as_string())
        del msg["To"]  # Remove for next loop

print("Emails sent successfully.")