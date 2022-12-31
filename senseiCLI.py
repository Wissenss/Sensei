import argparse
from pathlib import Path
import os

#external modules
from termcolor import colored

parser = argparse.ArgumentParser(description="This is the sensei bot command line interfaze, control and administer your bot all from one place!")
parser.add_argument("initializeDb")

# inizialization
os.system("color")
os.system("cls")
print(colored("=========================================================================", "white"))
print(colored("=======", "white"), colored("            Sensei Bot Command Line Interface            ", "cyan"), colored("=======", "white"))
print(colored("=======", "white"), colored("                      wissens 2022                       ", "cyan"), colored("=======", "white"))
print(colored("=========================================================================", "white"))

#local modules
from database import Database

print("reading configuration file...")

