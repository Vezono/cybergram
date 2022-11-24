from threading import Thread

import requests
import wolframalpha
from pyrogram import Client
from pyrogram import types
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

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
        options.add_argument('window-size=1000x100')
        self.driver = Chrome(service=Service(ChromeDriverManager().install()), options=options)

    async def get_wolfram_text(self, text):
        req_en = urllib.parse.quote_plus(text)
        vgm_url = 'https://www.wolframalpha.com/input?key=&i=' + req_en
        self.driver.get(vgm_url)
        try:
            myElem = WebDriverWait(self.driver, 40).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, '_13aP')))
        except TimeoutException:
            print("Loading took too much time!")
        self.driver.execute_script("document.body.innerHTML = document.getElementsByClassName('_1vuO')[0].innerHTML")
        required_width = self.driver.execute_script('return document.body.parentNode.scrollWidth')
        required_height = self.driver.execute_script('return document.body.parentNode.scrollHeight')
        self.driver.set_window_size(required_width, required_height)
        res = self.driver.find_element(By.TAG_NAME, 'body').screenshot_as_png
        self.driver.set_window_size(1000, 100)
        return res, required_height

    async def execute(self, c: Client, m: types.Message):
        if not self.wclient:
            self.wclient = wolframalpha.Client(c.user.storage.config['wolfram'])

        if ".w s " in m.text:
            req= m.text.replace(".w s ", "")
            await m.delete()
            pic, length  = await self.get_wolfram_text(req)
            img_obj = Image.open(BytesIO(pic))
            img_obj.save("resources/some.png")
            if length > 1200:
                await c.send_document(m.chat.id, "resources/some.png")
            else:
                await c.send_photo(m.chat.id, "resources/some.png")
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
