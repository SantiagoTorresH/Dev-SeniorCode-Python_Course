    #! singleton garantiza que solo exista un objeto de su tipo 

# class singleton:
#     _instance = None
    
    
#     def __new__cls(cls, *args, **kwargs):
#         if not cls._instance:
#             cls._instance = super(singleton, cls).__new__(cls, *args, **kwargs )
#         return cls._instance    
            


import sqlite3

class DatabaseConnection:
    
    _instances = {}
    
    def __new__(cls, *args, **kwargs):
        if  not cls._instances:
            cls._instances = super(DatabaseConnection, cls).__new__(cls, *args, **kwargs)
            cls._instances.connection = None
        return cls._instances   
    
    # def __init__(self):  
    #     self.connection = None
    
    def connect(self, database_name):
        if self.connection is None:
            self.connection = sqlite3.Connection(database_name)
            print(f"Conectado a la base de datos {database_name} ")
            
        else:
            print("Ya existe una conexion activa ")  
        return self.connection
    
    def close_connection(self):
        if self.connection:
            self.connection.close()
        print("Conexion cerrada")
        self.connection = None
        
db1 = DatabaseConnection()
connection1 = db1.connect("Mi_base_de_datos.db")


db2 = DatabaseConnection()
connection2 = db2.connect("Otra_base_de_datos.db")

print(db1 == db2)

db1.close_connection()    
db2.close_connection()    