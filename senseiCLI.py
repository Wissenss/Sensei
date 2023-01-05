#built in module
import os
import sys

#external modules | this should be pip installed
from termcolor import colored

#local modules
from database import dataModule, intf
from arg_parser import parser
from errors import ErrorCode, ErrorMessage, Error
from config import Settings

""" Inicialization """
os.system("color")
# os.system("cls")
size = os.get_terminal_size()
width = size.columns
borderWidth = width//10
print(colored("="*width, "white"), end="\n")
print(colored("="*borderWidth, "white"), colored('{:^{}}'.format("Sensei Bot Command Line Interface", width-(2*borderWidth)-2), "cyan"), colored("="*borderWidth, "white"), end="\n")
print(colored("="*borderWidth, "white"), colored('{:^{}}'.format("2022-2023 ", width-(2*borderWidth)-2), "cyan"), colored("="*borderWidth, "white"), end="\n")
print(colored("="*width, "white"), end="\n\n")

""" Command Handler """
#no argument for the utility
if len(sys.argv)==1:
    ErrorMessage[ErrorCode.ERR_NO_ARGUMENT_PROVIDED].printError()
    sys.exit(1)

args = parser.parse_args()
subcommand = args.subcommand

if subcommand == "config":
    action = args.action

    if action=="show":
        configfile = Settings()
        errors = configfile.load()

        #print config file contents
        print(" Reading configuration files... ")
        sections = configfile.sections()
        for section in sections:
            print("\n  " + colored(f"{section}", "cyan") +"")
            # print([option for option in configfile[section]])
            for option in configfile[section]:
                value = configfile.get(section, option)
                print("    "+colored(option, "white")+": "+value)

        if errors!=ErrorCode.ERR_NO_ERROR:
            for error in errors:
                ErrorMessage[error].printError()

        sys.exit(1)

    if action=="init":
        answer = input("  This procedure will \033[41moverwrite your configuration file\033[0m, do you want to proceed? \n  (y/n): ")
        if not(answer in ["y", "Y"]):
            sys.exit()

        settings = Settings()
        settings.set_default()

        #asking for discord token
        print("\n  Please provid the following values")
        token = input("    \033[36mDiscord Token\033[0m: ")
        #it would be nice to add some validation for tokens, not a priority tho
        settings.set("DISCORD", "token", token)
        
        print("\n  saving...")
        settings.store()
        sys.exit()

if subcommand == "database":
    action = args.action

    if action in ["init"]:
        # response = input(" This procedure will \033[41mreset you configfile\033[0m, do you want to proceed?\n (y|n): ")
        # if response != "y":
        #     print(" \naborting procedure...")
        #     sys.exit(1)

        print(" reading settings...\n")
        configfile = Settings()
        errors = configfile.load()
        if errors != ErrorCode.ERR_NO_ERROR:
            print(errors)
            sys.exit()

        print(" initializing database...")
        dataModule.DataModule.instancepath = configfile.get("DATABASE", "path")
        import database.init_db #initialize db

        # configfile.store()
        print("\n terminating process...")
        sys.exit(1)

if subcommand == "bot":
    action = args.action

    if action in ["run"]:
        print("running bot...")
        # os.system("python discord/main.py")
        # execfile("discord/main.py")
        # os.startfile("discord/main.py")
        # os.system("start cmd python discord/main.py")
        # subprocess.call("python discord/main.py", creationflags=subprocess.CREATE_NEW_CONSOLE)
        # os.popen("python discord/main.py")
        os.system("start cmd /k python senseiBot.py")
        sys.exit(1)

#the argument does not match any sub command
print(f"\"{subcommand} {action}\" is not a valid command, type -h for a list of available commands")