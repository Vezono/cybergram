import time
from threading import Thread
import schedule

from src.core import User
from pyrogram import idle


def some():
    while True:
        schedule.run_pending()
        time.sleep(1)


open('accounts.txt', 'a').close()
with open('accounts.txt') as f:
    accounts = f.read().splitlines()
for account in accounts:
    User(account)
Thread(target=some).start()
idle()
