"""MODULES"""
from email import message
import discord #discord module
from discord.ext import commands

import logging  #discord.py logs errors and debug information via the logging python module
import sqlite3  #database module

from dotenv import load_dotenv #hide TOKEN as enviorment variable
import os 

"""CUSTOM CLASSES"""
from members import User

"""CONFIGURATION"""
load_dotenv() #loads .env variables
TOKEN = os.getenv("TOKEN") #reads TOKEN, store at .env

logging.basicConfig(level=logging.INFO) #set logging to basic config

intents = discord.Intents.default() #set Intents to default
client = commands.Bot(intents=intents, command_prefix = '!') #instance Bot object, set prefix to !

#connect to database database.db
connection = sqlite3.connect('database.db')

"""COMMANDS"""
@client.event   #logging log
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.command()   #display bot information on server, read from message/info.txt
async def info(ctx):
    #read info.txt
    file = open('assets/messages/info.txt', 'r')
    message = file.read()
    file.close()

    #display message on server
    await ctx.send(message)

@client.command()   #display user information, store on records.db in "records" table
async def status(ctx):
    #creates instance of user
    user = User(ctx.message.author, connection)

    #display user information on server
    await ctx.send(f"**{user.username}**")
    await ctx.send(f"**Score:** *{user.score}*")
    await ctx.send(f"**Money:** *{user.money}*")

@client.command()
async def deck(ctx):
    #create instance of user
    user = User(ctx.message.author, connection)

    #create message
    message = "**Name   Number   Value   Element   Color**"

    #   acces User inventory
    for card in user.deck_inventory.row_get_all():
        message += '\n'
        for element in card:
            message += f"{element}   "
    
    #display message on server
    await ctx.send(message)

@client.command()
async def arquitecture(ctx):
    #read info.txt
    file = open('assets/messages/arquitecture.txt', 'r')
    message = file.read()
    file.close()

    #display message on server
    await ctx.send(message)

client.run(f'{TOKEN}')