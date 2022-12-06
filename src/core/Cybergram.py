import tomli
from src.user import User
from pyrogram import idle

open("accounts.toml", 'a').close()
with open("accounts.toml", mode="rb") as fp:
    accounts = tomli.load(fp)

class Cybergram:
    def __init__(self):
        self.users = []

    @property
    def user_ids(self):
        return [user.client.id for user in self.users]

    def run(self):
        for account in accounts:
            if account == 'config':
                continue
            api_id = accounts[account]['api_id'] if accounts[account].get('api_id') else accounts['config']['api_id']
            api_hash = accounts[account]['api_hash'] if accounts[account].get('api_hash') else accounts['config']['api_hash']
            self.users.append(User(account, api_id, api_hash))
        idle()

    def get_user(self, user_id):
        for user in self.users:
            if user.client.id == user_id:
                return user

cybergram = Cybergram()
    