import argparse
import sys

# class customParser(argparse.ArgumentParser):
#     def error(self, message="test"):
#         sys.stderr.write('error: %s\n' % message)
#         self.print_help()
#         sys.exit(2)

parser = argparse.ArgumentParser()
sub_parsers = parser.add_subparsers(dest="subcommand")

"""config sub command"""
config_parser = sub_parsers.add_parser("config")
config_parser.add_argument("action")

"""database sub command"""
database_parser = sub_parsers.add_parser("database")
database_parser.add_argument("action")
database_parser.add_argument("--sql", default="")

"""bot sub command"""
bot_parser = sub_parsers.add_parser("bot")
bot_parser.add_argument("action")