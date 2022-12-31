import discord
from discord.ext import commands

from config import settings

# intents = discord.Intents.default()
# client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix="$")

@bot.event
async def on_ready():
    print(f"succesful login as {bot.user}")

@bot.command()
async def stats(ctx, args ):
    await ctx.send("wololo")

bot.run(settings.TOKEN)