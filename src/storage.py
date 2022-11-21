from os.path import exists
from os import mkdir
import json

from pyrogram.types import Message

from src import constants


class StorageCore:
    def __init__(self, name):
        self.name = name
        self.initialize_files()
        self.path = f'accounts/{self.name}/{self.name}'

        self.api_id = self.config['api_id']
        self.api_hash = self.config['api_hash']

    @property
    def config(self):
        return self.load_json('config.json')

    def jsonize(self, m):
        return json.loads(str(m))

    def ignored(self, m):
        if not m.chat:
            return False
        if m.chat.id in self.config['ignore_chats']:
            return True

    def initialize_files(self):
        if not exists('accounts'):
            mkdir('accounts')
        if not exists(f'accounts/{self.name}'):
            mkdir(f'accounts/{self.name}')
        for json_file in constants.files:
            if exists(f'accounts/{self.name}/{json_file}'):
                continue
            self.create_json(json_file)

    def load_json(self, json_file):
        json_file = f'accounts/{self.name}/{json_file}'
        with open(json_file, "r") as read_file:
            data = json.load(read_file)
        return data

    def write_json(self, json_file, data):
        json_file = f'accounts/{self.name}/{json_file}'
        with open(json_file, "w") as write_file:
            json.dump(data, write_file)

    def create_json(self, json_file):
        self.write_json(json_file, {})
