#!/usr/bin/python3
import smtplib
from email.message import EmailMessage
import ssl

def login(cred_file):
    user_pass = []
    with open(cred_file, "r") as credentials:
        for line in credentials:
            user_pass.append(line.strip())
    return user_pass

def send_email(creds, recipient, email_attachment):
    context = ssl.create_default_context()
    message = EmailMessage()
    message["From"] = creds[0]
    message["Subject"] = "Weather Report!"
    message["To"] = recipient
    message.set_content("Your weather report for today is: ")
    message.add_attachment(open(email_attachment, "r").read(), filename="Weather_attachment.txt")
    smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465,context=context)
    smtp_server.login(creds[0], creds[1])
    smtp_server.send_message(message)
