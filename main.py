import discord
from discord.ext import commands

import logging  #discord.py logs errors and debug information via the logging python module
import sqlite3  #database module

from dotenv import load_dotenv
import os

load_dotenv() 
TOKEN = os.getenv("TOKEN")

logging.basicConfig(level=logging.INFO) #set logging to basic config

intents = discord.Intents.default()

client = commands.Bot(intents=intents, command_prefix = '!')

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.command()
async def status(ctx):
    connection = sqlite3.connect('records.db')
    records = connection.cursor() 

    player = ctx.message.author 
    records.execute(f"SELECT * FROM records WHERE user = '{player}'")
    info = records.fetchone()

    if(not info):
        records.execute(f"INSERT INTO records VALUES ('{player}',0,0)")
        connection.commit()

    await ctx.send(f"**{info[0]}**")
    await ctx.send(f"**Score:** *{info[1]}*")
    await ctx.send(f"**Money:** *{info[2]}*")
    connection.close()

client.run(f'{TOKEN}')