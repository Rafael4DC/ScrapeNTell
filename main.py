#!/usr/bin/env python
import datetime
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import discord
from discord.ext import commands
import asyncio

# This generates options automatically from the options.py file
# and passes them to the Chrome class automatically

intents = discord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix='!', intents=intents)

CHROME_PATH = '/usr/bin/google-chrome'
CHROMEDRIVER_PATH = "libs/chromedriver.exe"
WINDOW_SIZE = "1920,1080"

notify_list = []
chrome_options = Options()
chrome_options.add_argument("--headless=new")
time_last = datetime.datetime.now()


# event that triggers when the bot is ready to receive commands
@client.event
async def on_ready():
    print('Bot is ready')


@client.command()
async def ping_me(ctx):
    user = ctx.author
    if user in notify_list:
        await user.send("NT dingus")
    else:
        notify_list.append(user)


async def website_check(ctx):
    global time_last
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
            if time_last + datetime.timedelta(seconds=600) <= datetime.datetime.now():
                channel = client.get_channel(1)
                await channel.send('Big Chilling as of ' + str(datetime.datetime.now()))
                print("The lists are equal")
                time_last = datetime.datetime.now()
        else:
            for user in notify_list:
                await user.send("RAPIDO VAI VER https://www.warhammer-community.com/en-us/latest-news-features/")
        sleep(10)  # time in seconds
        print("Still sleeping")
        sleep(100)

@client.command()
async def do_monitor(ctx):
    asyncio.create_task(website_check(ctx))
    print("monitor started")


client.run('MTEwNjM3NjQ0MjEyOTk0MDQ5MA.GbJBMa.OvyRJA-TNhPHyQe1bUGbob0h3YG2hugSztvQ6M')
