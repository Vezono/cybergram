from pyrogram import Client, filters
from pyrogram.handlers import *
from src.logger import Logger

app = Logger()
client = Client("vezono", api_id=app.config['api_id'], api_hash=app.config['api_hash'])