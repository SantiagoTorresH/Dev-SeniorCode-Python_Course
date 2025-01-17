productos = [
    {"nombre": "Laptop", "precio": 1500},
    {"nombre": "celular", "precio": 500},
    {"nombre": "Tablet", "precio": 2000},
]

productos_filtro = filter(lambda x:x["precio"] < 1000, productos)

productos_ordenados =sorted(productos_filtro, key=lambda x: x["precio"])
print(productos_ordenados)
