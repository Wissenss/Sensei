from .initializeDb import initialize
from config import SettingsReader

class Database:
    def __init__(self, settings:SettingsReader):
        path = settings.InstancePath

    def openConnection(self):
        pass

    def closeConnection(self):
        pass

    def initialize(self):
        initialize()