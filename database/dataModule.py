import sqlite3

class DataModule(sqlite3.Connection):
    instancepath = None
    
    def __init__(self):
        self.connect()

    def setinstancepath(self, path):
        #falta, agregar validacion para el path
        DataModule.instancepath = path

    def connect(self):
        super().__init__(DataModule.instancepath)

    def disconnect(self):
        self.close()
