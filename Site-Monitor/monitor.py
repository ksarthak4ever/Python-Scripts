import os #to import the environment variables
import smtplib
import requests
from linode_api4 import LinodeClient, Instance

EMAIL_ADDRESS = os.environ.get('EMAIL_USER') 
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
LINODE_TOKEN = os.environ.get('LINODE_TOKEN')


def notify_user():

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        subject = 'YOUR SITE IS DOWN!'
        body = 'Make sure the server restarted and it is back up'
        msg = f'Subject: {subject}\n\n{body}'


        smtp.sendmail(EMAIL_ADDRESS, 'ksarthak4ever@gmail.com', msg) # i.e (<senders email>, <receivers email>, mail message)


def reboot_server():

    client = LinodeClient(LINODE_TOKEN)
    my_server = client.load(Instance, 376715)   #to get the id of the server simply :~ for linode in client.linode.instances():
                                                #                                          print(f'{linode.label}: {linode.id}')  and get the id for that server.
    my_server.reboot() 

try:
    r = requests.get('https://sarthakkumar.me', timeout=5)

    if r.status_code != 200: #i.e site is down
        notify_user()
        reboot_server()

except Exception as e: # as sometimes server goes down and we dont even get a response code.
    notify_user()
    reboot_server()