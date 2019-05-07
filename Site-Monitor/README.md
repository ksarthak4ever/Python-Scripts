# Site-Monitor

This is a Python script to check if the server of a website (in this case my portfolio) is down and send an email if the server is down and restarts the server. Note :~ For this script the server is supposed to be linode,you can refer to other servers api docs to do the same in them.

## Libraries Used

* [smtplib](https://docs.python.org/3/library/smtplib.html) 

* [requests](https://2.python-requests.org/en/master/)

* [linode_api4](https://linode-api4.readthedocs.io/en/latest/)

## Things to Note

To send the mail you will have to use an mail server such as gmail and such. I'm using my gmail account here. Whatever server you are using you will have to look up the instructions online on how to connect to that server. For gmail it is pretty simply you need to let gmail know you will be connecting to your account through an program.

* [If you dont have two factor authentication set up](https://myaccount.google.com/lesssecureapps)

* [If you have two factor authentication set up](https://myaccount.google.com/apppasswords?rapt=AEjHL4OwXFQeTQ_7QmnP98X5tcA2QqTrh__YFb4vO9M6svVyVc6MlTRwDOENZpvUGA5zOGIspQAxH2BXVP9OqihN09SPVGUIUA)

## Making Script run every 10 minutes

You can use `crontab -e` to create a user cron schedule. Once inside the editor after entering the previous command you should enter the command(i.e The line you specifically need is) :~

* `*/10 * * * * /home/Python-Scripts/my_env/bin/python /home/Python-Scripts/Site-Monitor/monitor.py ` 

Here /10 is telling to tell command every ten minutes and after that each asterisk mark denotes hours,days,months,years respectively. After that i am defining the python version used in my virtualenv  and then finally the command for script.

To Check all the crontab schedule simply give command :~ `crontab -l`
