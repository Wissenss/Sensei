import os
import discord
# from discord.ext import commands this will be implemented later
import logging
import logger #configure the logging module
from termcolor import colored

# local modules
from config import Settings 
import commands
from database.dataModule import DataModule

#initialization message
os.system("") #this is because ansi escape sequences wont work otherwhise
os.system("cls")
size = os.get_terminal_size()
width = size.columns
borderWidth = width//10
print(colored("="*width, "white"), end="\n")
print(colored("="*borderWidth, "white"), colored('{:^{}}'.format("Sensei Bot", width-(2*borderWidth)-2), "cyan"), colored("="*borderWidth, "white"), end="\n")
print(colored("="*borderWidth, "white"), colored('{:^{}}'.format("2022-2023 ", width-(2*borderWidth)-2), "cyan"), colored("="*borderWidth, "white"), end="\n")
print(colored("="*width, "white"), end="\n\n")

#settings
settings = Settings()
settings.load()

#database configurations
DataModule.instancepath = settings.get("DATABASE", "path")

#bot configuration
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    logging.info(f"succesfully logged as \033[95m{client.user}\033[0m")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #help
    if message.content.startswith("!help"):
        logging.info(f"\033[94mhelp\033[0m command called by \033[95m{message.author}\033[0m")
        await commands.help(message)

    #hello
    if message.content.startswith("!hello"):
        logging.info(f"\033[94mhello\033[0m command called by \033[95m{message.author}\033[0m")
        await commands.hello(message)

    #status
    if message.content.startswith("!status"):
        logging.info(f"\033[94mstatus\033[0m command called by \033[95m{message.author}\033[0m")
        await commands.status(message)

#run bot
client.run(settings.get("DISCORD", "token"), log_handler=None)