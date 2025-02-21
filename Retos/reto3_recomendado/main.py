import tkinter as tk
from tkinter import messagebox,ttk
from operaciones import agregar_producto_historia_venta, calcular_total
from excepciones import manejo_errores
from productos import productos, calcular_total


# configuracion de la interfaz
ventana = tk.Tk()
ventana.title("Caja Registradora - Tienda Fruber")

# marco principal 
marco_principal = tk.Frame(ventana, padx=30, pady=30, bg='#f4f4a2')
marco_principal.pack(fill= 'both', expand=True)

#Titulo
titulo = tk.Label(marco_principal, text="Bienvenido a la tienda fruber", font=("Arial", 20), bg='#fff1f8', fg='green')
titulo.grid(row=0, column=0, padx=10, pady=10 )

# Frame para lista de productos
frame_productos = tk.Frame(ventana, padx=30, pady=30, bg='#f4f4a2')
frame_productos.grid(row=1, column=0, padx=10, pady=10 )

# TreeView
etiqueta_lista_productos = tk.Label(frame_productos, text="Seleccion un producto", font=("Arial", 14), bg='#f343')
etiqueta_lista_productos.pack(pady= 10)

treeview_productos = ttk.Treeview(frame_productos, columns=("Productos", "Precio", "CAntidad Disponible"), ahow="headings", height=10 )
treeview_productos.heading("Producto", text="Producto " )
treeview_productos.heading("Precio", text="Precio")
treeview_productos.heading("Cantidad Disponible", text="Cantidad Disponible")
treeview_productos.column("Producto")
treeview_productos.column("Precio")
treeview_productos.column("Cantidad Disponible")


# Insertar productos e el TreeView
for key, producto in productos.items():
    cantidad_disponible = 100
    treeview_productos.insert("", "end", idd=str(key), values=(producto['nombre'], f"${producto['precio']}, cantidad_disponible"))
    
treeview_productos.pack(pady=10)

# Frame para la cantidad y el boton
frame_cantidad  = tk.Frame(marco_principal, bg="#f4f4f9")
frame_cantidad.grid(row=1, column=1, padx=10, pady=10)

# campo por la cantidad
etiqueta_cantidad = tk.Label(frame_cantidad, text="Cantidad", font=("Arial",14), bg="#f4f4f9") 
etiqueta_cantidad.pack(pady=10)


ventana.mainloop()  

    
    
