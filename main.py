"""MODULES"""
import discord #discord module
from discord.ext import commands

import logging  #discord.py logs errors and debug information via the logging python module
import sqlite3  #database module

from dotenv import load_dotenv #hide TOKEN as enviorment variable
import os 

"""CONFIGURATION"""
load_dotenv() #loads .env variables
TOKEN = os.getenv("TOKEN") #reads TOKEN, store at .env

logging.basicConfig(level=logging.INFO) #set logging to basic config

intents = discord.Intents.default() #set Intents to default
client = commands.Bot(intents=intents, command_prefix = '!') #instance Bot object, set prefix to !

"""COMMANDS"""
@client.event   #logging log
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.command()   #display bot information on server, read from message/info.txt
async def info(ctx):
    #read info.txt
    file = open('messages/info.txt', 'r')
    message = file.read()
    file.close()

    #display message on server
    await ctx.send(message)

@client.command()   #display user information, store on records.db in "records" table
async def status(ctx):
    #connect to database records.db
    connection = sqlite3.connect('records.db') 
    records = connection.cursor() 

    #search for user in "records" table
    player = ctx.message.author 
    records.execute(f"SELECT * FROM records WHERE user = '{player}'") 
    info = records.fetchone()

    #check if user already exist
    if(not info):       
        #if not, add user to database with default values
        records.execute(f"INSERT INTO records VALUES ('{player}',0,0)")
        connection.commit()

    #display user information on server
    await ctx.send(f"**{info[0]}**")
    await ctx.send(f"**Score:** *{info[1]}*")
    await ctx.send(f"**Money:** *{info[2]}*")
    connection.close()

client.run(f'{TOKEN}')