import os
from configparser import ConfigParser
from errors import ErrorCode
CONFIG_FILE = "config.ini"

class Settings(ConfigParser):
    def __init__(self):
        super().__init__()
        #init parser with default values, this will be overwrriten by with the ones stored in config.ini
        self.add_section("DISCORD")
        self.set("DISCORD", "token", "")

        self.add_section("DATABASE")
        self.set("DATABASE", "path", "database.db") 

        self.add_section("CLI")
        self.set("CLI", "highlight color", "cyan")
        self.set("CLI", "font color", "white")
    
    #reads the contents of the parser from config.ini
    def load(self):
        self.read(CONFIG_FILE)
        return self._isvalidconfig()

    #write the contents of the parser to config.ini 
    def store(self):
        with open(CONFIG_FILE, "w") as configfile:
            self.write(configfile)

    def _isvalidconfig(self, configparser:ConfigParser=None):
        configparser = self if configparser == None else configparser
        errors = []

        #discord validations
        discord = configparser["DISCORD"]
        token = discord.get("token")
        if not(self.__isvalidtoken(token)):
            errors.append(ErrorCode.ERR_INVALID_CONFIG_TOKEN)

        #database validations
        database = configparser["DATABASE"]
        path = database.get("path")
        if not(self.__isvalidpath):
            errors.append[ErrorCode.ERR_INVALID_CONFIG_PATH]

        #cli validations

        return ErrorCode.ERR_NO_ERROR if errors == [] else errors

    # validation functions
    # discord config
    def __isvalidtoken(self, token):
        if not(isinstance(token, str)):
            return False

        if not(len(token)==59 or len(token)==70):
            return False

        return True

    # database config
    def __isvalidpath(self, path):
        if not(os.path.isfile(path) or os.path.isdir(path)):
            return False

    # cli config

