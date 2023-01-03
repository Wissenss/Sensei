from enum import Enum
from termcolor import colored

class ErrorCode(Enum):
    # the error code is:
    # {00}{00}{00}
    # {type}{sub-type}{number}

    # no error return value
    ERR_NO_ERROR = "000000"
    # general cli errors 01 ## ##
    ERR_NO_ARGUMENT_PROVIDED = "010101"

    # config file errors 02 ## ##
    #   discord config 02 01 ##
    ERR_INVALID_CONFIG_TOKEN = "020101"

    #   database config 02 02 ##
    ERR_INVALID_CONFIG_PATH = "020201"
    
    #   cli config 02 03 ##

    # database operations errors 03 ## ##
    #   Players Table 03 01 ##
    ERR_RECORD_ALREADY_EXISTS_PLAYERS = "030101" 
    ERR_RECORD_NOT_FOUND_PLAYERS = "030102"

class Error:
    def __init__(self, errorCode, cause, indication):
        self.errorCode = errorCode
        self.cause = cause
        self.indication = indication

    def printError(self):
        print(colored(f"\n  {self.errorCode}: {self.cause}! {self.indication}.\n", "red"))

ErrorMessage = {}
#010101
ErrorMessage[ErrorCode.ERR_NO_ARGUMENT_PROVIDED] = Error(ErrorCode.ERR_NO_ARGUMENT_PROVIDED, "No argument", "Run senseiCLI with -h flag for a list of available commands")

#020101
ErrorMessage[ErrorCode.ERR_INVALID_CONFIG_TOKEN] = Error(ErrorCode.ERR_INVALID_CONFIG_TOKEN, "Not a valid token", "Make sure that your token is correct")

#020201
ErrorMessage[ErrorCode.ERR_INVALID_CONFIG_PATH] = Error(ErrorCode.ERR_INVALID_CONFIG_PATH, "Not a valid path", "make sure the configured path exists and is accesible by the application")