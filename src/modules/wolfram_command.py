from threading import Thread

import requests
import wolframalpha
from pyrogram import Client
from pyrogram import types
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from src.BaseCommand import BaseCommand
import urllib.parse
from bs4 import BeautifulSoup
from requests_html import AsyncHTMLSession
from selenium.webdriver import Chrome
from selenium import webdriver
from PIL import Image
from io import BytesIO

class WolframCommand(BaseCommand):
    def __init__(self):
        super().__init__('w')
        self.wclient = None
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=800x800')
        self.driver = Chrome(executable_path="./chromedriver.exe", options=options)

    async def get_wolfram_text(self, text):
        req_en = urllib.parse.quote_plus(text)
        vgm_url = 'https://www.wolframalpha.com/input?key=&i=' + req_en
        self.driver.get(vgm_url)
        try:
            myElem = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, '_13aP')))
        except TimeoutException:
            print("Loading took too much time!")
        self.driver.execute_script("window.scrollTo(0, 400)")
        return self.driver.get_screenshot_as_png()

    async def execute(self, c: Client, m: types.Message):
        if not self.wclient:
            self.wclient = wolframalpha.Client(c.user.storage.config['wolfram'])

        if ".w s " in m.text:
            req = m.text.replace(".w s ", "")
            await m.delete()
            pic = await self.get_wolfram_text(req)
            img_obj = Image.open(BytesIO(pic))
            img_obj.save("some.png")
            await c.send_photo(m.chat.id, photo="some.png")
        else:
            req = m.text.replace(".w", "")
            await m.edit(f'Request: {req}\nAnswer: Loading...')
            res = self.wclient.query(req)
            text = ""
            for pod in res.results:
                text += pod.text + "\n"
            if text:
                await m.edit(f'Request: {req}\nAnswer: {text}')
            else:
                await m.edit(f'Request: {req}\nAnswer: Nothing found!')


commands = [WolframCommand]
listeners = []
