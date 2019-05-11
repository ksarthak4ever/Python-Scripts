import smtplib

import config


def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        message = f'Subject: {subject}\n\n{body}'
        server.sendmail(config.EMAIL_ADDRESS, config.EMAIL_ADDRESS, message) # i.e (<senders email>, <receivers email>, mail message)
        server.quit()
        print("Success: Email sent!")
    except:
        print("Email failed to send.")


subject = "Test subject"
msg = "Hello there, this is Sarthak"

send_email(subject, msg)