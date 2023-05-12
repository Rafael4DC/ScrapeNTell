#!/usr/bin/env python
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import discord
from discord.ext import commands

# This generates options automatically from the options.py file
# and passes them to the Chrome class automatically

intents = discord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix='!', intents=intents)

CHROME_PATH = '/usr/bin/google-chrome'
CHROMEDRIVER_PATH = "chromedriver.exe"
WINDOW_SIZE = "1920,1080"

notify_list = []
chrome_options = Options()
chrome_options.add_argument("--headless=new")


# event that triggers when the bot is ready to receive commands
@client.event
async def on_ready():
    print('Bot is ready')



# command to send a private message
@client.command()
async def hook_me_to_the_main_frame(ctx):
    user = ctx.author
    if user in notify_list:
        await user.send("NT dingus")
    else:
        notify_list.append(user)
        await user.send("You have been added to the notification list.")
        new_text = ""
        old_text = ""
        while True:
            old_text = new_text
            driver = webdriver.Chrome(CHROMEDRIVER_PATH, options=chrome_options)

            url = 'https://www.warhammer-community.com/en-us/latest-news-features/'

            # to open the url in the browser
            driver.get(url)
            elements = driver.find_elements(By.XPATH, '/html/body/div[1]/div[3]/div[2]')
            for element in elements:
                new_text = element.text

            # Close Chrome
            driver.close()

            if new_text == old_text:
                print("The lists are equal")
            else:
                user = ctx.author
                await user.send("RAPIDO VAI VER https://www.warhammer-community.com/en-us/latest-news-features/")
            sleep(1000)#time in seconds


client.run('MTEwNjM3NjQ0MjEyOTk0MDQ5MA.GbJBMa.OvyRJA-TNhPHyQe1bUGbob0h3YG2hugSztvQ6M')
