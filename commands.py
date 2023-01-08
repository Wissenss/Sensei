from random import randint

from discord.message import Message 
from discord import Embed, Color

from database import intf
from errors import ErrorCode
import commands_utils

async def help(message: Message):
    commands = {
        "!help": "show this message",
        "!hello": "say hi to sensei",
        "!status": "display your current stats",
        "!belts": "get a list of all belts available"
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
    beltColors = {
        None : Color.from_rgb(47, 49, 54),
        "Black" : Color.from_rgb(49, 55, 61), 
        "Brown" : Color.from_rgb(193, 105, 79),
        "Purple" : Color.from_rgb(170, 142, 214),
        "Red" : Color.from_rgb(221, 46, 68),
        "Blue" : Color.from_rgb(85, 172, 238),
        "Green" : Color.from_rgb(120, 177, 89),
        "Orange" : Color.from_rgb(244, 144, 12),
        "Yellow" : Color.from_rgb(253, 203, 88),
        "White" : Color.from_rgb(230, 231, 232),
    }

    #query database
    error, playerRecord = intf.get_player(message.author)
    if error == ErrorCode.ERR_RECORD_NOT_FOUND_PLAYERS:
        error, playerRecord = intf.add_player(message.author)

    #player info
    score = playerRecord[1]  #wack, deberia haber mejor manera
    capital = playerRecord[2]
    name = message.author.name

    #get the corresponding color
    player_color = commands_utils.current_ninjarank(score)

    #create embed
    embed = Embed(title=name)
    embed.add_field(name="Score", value=score, inline=True)
    embed.add_field(name="Capital", value=capital, inline=True)
    embed.add_field(name="Belt Progress", value=commands_utils.beltProgressBar(score, player_color), inline=False)
    embed.color = beltColors[player_color]

    #output stats
    await message.channel.send(embed=embed)

async def jitsu(message: Message):
    mention = message.mentions
    server = message.guild
    members = server.members

    await message.channel.send(f"{'-'.join(members)}")

async def belts(message: Message):
    #this dictionary asociates the label color with discord's emoji 
    beltColors = {
        "Black" : ":black_large_square:", 
        "Brown" : ":brown_square:",
        "Purple" : ":purple_square:",
        "Red" : ":red_square:",
        "Blue" : ":blue_square:",
        "Green" : ":green_square:",
        "Orange" : ":orange_square:",
        "Yellow" : ":yellow_square:",
        "White" : ":white_large_square:",
    }

    #get the player score
    error, playerRecord = intf.get_player(message.author)
    if error == ErrorCode.ERR_RECORD_NOT_FOUND_PLAYERS:
        error, playerRecord = intf.add_player(message.author)

    #get the corresponding color
    player_color = commands_utils.current_ninjarank(playerRecord[2])

    #creates embed for each of the belts in beltColors
    embed = Embed(title="Available Belts")
    for color in beltColors:
        if color == player_color:
            color_title = f">{color}"
        else:
            color_title = f" {color}"

        embed.add_field(name=color_title, value=(beltColors[color]+' ')*7, inline=True)

    player_color = "You haven't earn a belt yet!" if player_color == None else player_color
    embed.set_footer(text=f"Your current belt: {player_color}")

    await message.channel.send(embed=embed)

