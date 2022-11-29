from src.utils.update import update
update()

import time
from threading import Thread
import scheduler

from src.user import User
from pyrogram import idle
import tomli
from pyrogram.types import ReplyKeyboardMarkup

open("accounts.toml", 'a').close()
with open("accounts.toml", mode="rb") as fp:
    accounts = tomli.load(fp)

for account in accounts:
    if account == 'config':
        continue
    api_id = accounts[account]['api_id'] if accounts[account].get('api_id') else accounts['config']['api_id']
    api_hash = accounts[account]['api_hash'] if accounts[account].get('api_hash') else accounts['config']['api_hash']
    User(account, api_id, api_hash)
idle()
