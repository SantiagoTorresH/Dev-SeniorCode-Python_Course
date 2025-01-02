
# patron de diseno Singleton 
class SingletonCreacionInstancia:
    
    
    # singleton no usa metodos de instacnsia como el self , sino metodo de dclase 
    _instancia = None
    
    def __new__(cls, *args, **kwargs):  # hace las veces del constructor de una clase normal, es lo primero que ya a llamar para crear un solo objeto. 
    # args para lista kward diccionario
    
        if not cls._instancia:
            cls._intancia = super(SingletonCreacionInstancia, cls)._new_(cls)# objeto cls clase,  .. hereda todo las clases y metodos que puedo tener
        return cls._instancia
        
        