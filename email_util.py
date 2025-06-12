import os
import smtplib
import ssl


def send_email(user_message):
    host = "smtp.gmail.com"
    port = 465
    username = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')
    receiver = os.getenv('EMAIL')
    my_context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, user_message)
