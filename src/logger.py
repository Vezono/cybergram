from os.path import exists
import json

from pyrogram.types import Message

from src import constants


class Logger:
    def __init__(self):
        self.initialize_files()

    @property
    def config(self):
        return self.load_json('config.json')

    def jsonize(self, m):
        return json.loads(str(m))

    def handler(self, c, m: Message):
        if self.ignored(m):
            return
        chat_id = m.from_user.id
        if m.chat:
            chat_id = m.chat.id
        data = self.load_json('dump.json')
        data.update({f'{chat_id}_{m.id}': self.jsonize(m)})
        self.write_json('dump.json', data)

    def ignored(self, m):
        if not m.chat:
            return False
        if m.chat.id in self.config['ignore_chats']:
            return True

    def initialize_files(self):
        for json_file in constants.files:
            if exists(json_file):
                continue
            self.create_json(json_file)

    def load_json(self, json_file):
        with open(json_file, "r") as read_file:
            data = json.load(read_file)
        return data

    def write_json(self, json_file, data):
        with open(json_file, "w") as write_file:
            json.dump(data, write_file)

    def create_json(self, json_file):
        self.write_json(json_file, {})
