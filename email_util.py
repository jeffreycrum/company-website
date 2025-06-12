import configparser
import smtplib
import ssl

config = configparser.ConfigParser()
config.read('config.ini')


def send_email(user_message):
    host = "smtp.gmail.com"
    port = 465
    username = config['Settings']['email']
    password = config['Settings']['password']
    receiver = config['Settings']['email']
    print(username)
    my_context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, user_message)
