import smtplib
import ssl


def send_email(user_message):
    host = "smtp.gmail.com"
    port = 465
    username = "jeffrey.crum81@gmail.com"
    password = "boochoazmttcgpey"
    receiver = "jeffrey.crum81@gmail.com"
    my_context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, user_message)
