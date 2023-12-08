import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "2004.zainsaleem@gmail.com"
    password = "hrob psxg asds gnqv"

    receiver_email = "2004.zainsaleem@gmail.com"
    context = ssl.create_default_context()
    message = message
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver_email, message)


