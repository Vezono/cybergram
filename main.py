import time
from threading import Thread
import scheduler

from user import User
from pyrogram import idle
import tomli

open("accounts.toml", 'a').close()
with open("accounts.toml", mode="rb") as fp:
    accounts = tomli.load(fp)
for account in accounts:
    User(account)
idle()
