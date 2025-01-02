# Polimorfismo a traves de metodos comunes en diferentes clases

class Gato:
    def sonido(self):
        return "Miau Miau"
    
    
class Carro:
    def sonido(self):   
        return "Pii piii" 
    
# primer polimorfismo mismo funcion o metodo, en diferentes clases

def hacer_sonido(objeto):
    print(objeto.sonido()) # puede recivir carro o gato
    
    # el sonido es el objeto 
    
# Instanciar es definir los objetos 
mi_gato = Gato()
mi_carro = Carro()  

# uso del poliformismo 
print(f"Mi gato hace el siguiente sonido: {hacer_sonido(mi_gato)}")

    