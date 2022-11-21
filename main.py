import time

import schedule

from user import User
from pyrogram import idle
from os.path import exists

open('accounts.txt', 'a').close()
with open('accounts.txt') as f:
    accounts = f.read().splitlines()
for account in accounts:
    User(account)

while True:
    schedule.run_pending()
    time.sleep(1)
