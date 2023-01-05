from random import randint

from discord.message import Message 
from discord import Embed

from database import intf
from errors import ErrorCode

async def help(message: Message):
    commands = {
        "!help": "show this message",
        "!hello": "say hi to sensei",
        "!status": "display your current stats",
    }
    
    embed = Embed(title="", color=0x000000)
    for command in commands:
        description = commands[command]
        embed.add_field(name=command, value=description, inline=False)

    await message.channel.send(embed=embed)

async def hello(message: Message):
    responses = [
        "Hello",
        "Hi there",
    ]
    await message.channel.send(responses[randint(0, len(responses)-1)])

async def status(message: Message):
    #query db
    error, playerRecord = intf.get_player(message.author)
    if error == ErrorCode.ERR_RECORD_NOT_FOUND_PLAYERS:
        error, playerRecord = intf.add_player(message.author)

    #create embed
    playerName = playerRecord[0] #wack, deberia haber mejor manera
    score = playerRecord[1]
    capital = playerRecord[2]
    embed = Embed(title=playerName)
    embed.add_field(name="score", value=score, inline=False)
    embed.add_field(name="capital", value=capital, inline=False)

    #output stats
    await message.channel.send(embed=embed)

async def jitsu(message: Message):
    mention = message.mentions
    server = message.guild
    members = server.members

    await message.channel.send(f"{'-'.join(members)}")