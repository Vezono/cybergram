from os.path import exists
from os import mkdir
import json

from pyrogram.types import Message

from src import constants


class Storage:
    def __init__(self, name):
        self.name = name
        self.type = type
        self.path = f'{self.type}/{self.name}/{self.name}'
        self.initialize_files()

        self.resources = {}

    @property
    def config(self):
        return self.load_json('config.json')

    def exists(self, file):
        return exists(f'{self.type}/{self.name}/{file}')

    def jsonize(self, m):
        return json.loads(str(m))

    def ignored(self, m):
        if not m.chat:
            return False
        if m.chat.id in self.config['ignore_chats']:
            return True

    def initialize_files(self):
        if not exists(f'{self.type}'):
            mkdir(f'{self.type}')
        if not exists(f'{self.type}/{self.name}'):
            mkdir(f'{self.type}/{self.name}')
        for json_file in constants.files:
            if exists(f'{self.type}/{self.name}/{json_file}'):
                continue
            self.create_json(json_file)

    def load_json(self, json_file):
        path = f'{self.type}/{self.name}/{json_file}'
        if not exists(path):
            self.create_json(json_file)
        with open(path, "r") as read_file:
            data = json.load(read_file)
        return data

    def write_json(self, json_file, data):
        path = f'{self.type}/{self.name}/{json_file}'
        with open(path, "w") as write_file:
            json.dump(data, write_file)

    def create_json(self, json_file):
        self.write_json(json_file, {})
