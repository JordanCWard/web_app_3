import smtplib
import os


def email_function(message):
    host = "smtp.gmail.com"
    port = 465

    # Python Mega Course lecture 221 to set this up
    username = "jordancward@gmail.com"

    # password is stored in environment variables
    password = os.getenv("PASSWORD")

    receiver = "moveshhh8@gmail.com"

    with smtplib.SMTP_SSL(host, port) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
