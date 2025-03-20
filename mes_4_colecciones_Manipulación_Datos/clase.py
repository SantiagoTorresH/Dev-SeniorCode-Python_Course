
#! Listas en python
productos = ["Carne", "Papa", "Tomate"] # array no existe en python 
productos.append("Yuca") 
print(productos)

lista = ["element1"]
lista.append("element2")
print(lista)



#! Tuplas en python 
Codigo_Postal = (45400, "Zipaquira")
print(Codigo_Postal)
#Codigo_Postal[0] = 45400
# print(Codigo_Postal)

empleado = (1010, "Luis Molero", "director") # las tuplas son inmutables
print(empleado) 
# empleado[1] = "San" # no soporta que cambiemos el item
# print(empleado) 


#! set (conjuntos) en python
categorias = {"Terror", "Drama", "ScFc"}
categorias.add("Suspenso")
print(categorias)

# Diccionarios (dict) en python

clientes = {
    "id": 1010,
    "Nombre": "Luis",
    "Apellido": "Molero"
}
print(clientes)
clientes["email"] = "Santiago@gmail.com"
print(clientes)