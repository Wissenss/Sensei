import discord

"TEMPORAL VARIABLES"
TOKEN = "ODczMTIzODYxMTEyMTc2NjUw.G5yHt8.QpyLezT8l3IaLf6RvqkN-c8UNAqd9j0vm4lAHE"

intents = discord.Intents.default()

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"succesful login as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("")

client.run(TOKEN)