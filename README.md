# Sensei
A discord bot to play card-jitsu. Host it yourself and run it in as many servers as you want... [To Do]

## Features
Sensei allows... [To Do]

Aditionally, a command line interfaze for general configuration and mantainance is included within the repository. Run it by typing:
```
python senseiCLI.py help
```
In the command prompt.

## How to run
A couple of python modules, configuration files and a database instance are needed for the application to run properly. W've provided a **setup.cmd** file that will automate the process of getting you setup up.

First of all, ensure that you have **python 3.8 or higher** installed and properly **added to path**. To check you python version run:
```
python --version
```
pip will also be necesary, if you installed python this should also be in you machine, make sure by typing:
```
pip --version 
```
in the command prompt. **This two should reference the same python version**.

Once thats done, run **setup.cmd** by double clicking the file. This will open a command prompt, install or upgrade all dependence python modules, ensure that configuration files exists and initialize a new instance of the database with all default values. When prompted with **Configuration File Overwrite** accept and wait until the procedure ends and the window close.

Now that's done, the following python modules will be install and upgraded:
- discord.py
- termcolor
- db-sqlite3

Also, two new files should appear on you project folder:

- **database.db** The bot database instance, this will store all realated data.
- **config.ini** The *.ini file, containing all personal configuration for CLI, database and bot behaviour.

Finally, a **discord bot application** is necesary to connect with the discord API, open **config.ini** and assing your token to the token attribute under the [DISCORD] section:
```ini
[DISCORD]
token = <your token goes here>
```
replace *\<your token goes here\>* with you personal token.

When creating you discord application make sure to **enable both message and memebers intends**. For more information in how to create a discord bot application, please refere to discord official documentation.

And that it! Type:
```
python senseiBot.py
```
and you sensei bot instance will launch. Have fun!
