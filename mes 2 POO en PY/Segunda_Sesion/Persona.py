class Persona:
    
    def __init__(self, nombre, edad):# init es un metodo constructor, ayuda con el proceso de encapsulamiento
        self.nombre = nombre# el self es la instancia
        self._edad = edad  # edad va protegido
        self.__cuentaBancaria = 1234  # esta como una constante, no se agrega como atributo, va privado
        
        
    
    def mostrarInformacion(self):
        return f"Nombre: {self.nombre} Edad: {self._edad}"
    
    def __mostrarCuenta(self):
        return f"cuenta Bancaria: { self.__cuentaBancaria}"
    
    def mostrarInformacioncompleta(self):
        return self.__mostrarCuenta()
    
persona1 = Persona("Santi", 45) # es la instancia, es el objeto que estoy creando. 

print(persona1.nombre)    
print(persona1._edad)    

print(persona1.mostrarInformacion())
print(persona1.mostrarInformacioncompleta())