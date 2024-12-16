import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()

def send_email(to: str, subject: str, body: str):
    sender = os.getenv('SENDER')
    pwd = os.getenv('GMAIL_PWD')

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = to

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as sender_email:
        sender_email.login(sender, pwd)
        sender_email.sendmail(sender, to, msg.as_string())

    print("The email has been sent!")

send_email("devkashkul@gmail.com", "Hello from python!", "Hello World!")