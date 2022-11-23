import time
from threading import Thread
import schedule

from user import User
from pyrogram import idle
import tomli

def some():
    while True:
        schedule.run_pending()
        time.sleep(1)


open("accounts.toml", 'a').close()
with open("accounts.toml", mode="rb") as fp:
    accounts = tomli.load(fp)
for account in accounts:
    User(account)
Thread(target=some).start()
idle()
