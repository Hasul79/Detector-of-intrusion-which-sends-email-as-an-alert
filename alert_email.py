import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import socket

def send_email(subject, body):
    ssender_email = "ваш_адрес_электронной_почты@gmail.com"
    receiver_email = "адрес_получателя@example.com"
    password = "ваш_пароль_от_почты"


    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

def detect_intrusion():
    try:
        socket.create_connection(("127.0.0.1", 80), timeout=2)
    except Exception:
        send_email("Intrusion Alert!", "This is my second project")
       

detect_intrusion()
