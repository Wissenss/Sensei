import os
from configparser import ConfigParser
FILEPATH = "config.ini"

class SettingsReader:
    def __init__(self):
        self.config = ConfigParser()
        self.TOKEN = None
        self.InstancePath = None

        try:
            self.readFile()
        except:
            self.createFile()
            self.configureFile()
            self.readFile()

    def readFile(self):
        self.config.read(FILEPATH)

        self.TOKEN = self.config.get("discord", "token")
        self.InstancePath = self.config.get("database", "instance path")

    def createFile(self, token="", instancePath="database/Dojo.db"):
        self.config.read(FILEPATH)
        self.config.add_section("discord")
        self.config.set("discord", "token", token)
        self.config.add_section("database")
        self.config.set("database", "instance path", instancePath)

        with open(FILEPATH, "w") as file:
            self.config.write(file)

    def configureFile(self):
        discordAppLink = "https://discordpy.readthedocs.io/en/stable/discord.html"
        print(f"Welcome! Thanks for downloading Sensei Bot source code\n\n\
This program is mean to be run locally to avoid conflicts while developing the application \
you should configure a personal discord application token to launch the bot, \
then you can invite that bot into your server and test as many new features and bug fixes as you wish. \
for more information about how to create a discord bot application go to: {discordAppLink}\n\n")

        print("Initializing configuration file...")
        print("Please provide the following parameters, you can change this later by editing config.ini\n")
        print("Discord API Values")
        token = input("token: ")

        print("Database Attributes")
        instancePath = input("instance path: ")

        self.config.set("discord", "token", token)
        self.config.set("database", "instance path", instancePath)
        with open(FILEPATH, "w") as file:
            self.config.write(file)

        print("Saving configuration file...")
        print("Running application...\n\n")