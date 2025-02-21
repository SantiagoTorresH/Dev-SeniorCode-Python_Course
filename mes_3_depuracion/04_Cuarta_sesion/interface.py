#Tkinter es una interface grafica, sustituye el terminal. 

import tkinter as tk

def convertir():
    try:
        celsius = float(entry.get())
        fahrenheit = (celsius * 9/5) + 32
        resultado.config(text= f"Resltado: {fahrenheit:.2f}~f ")
    except:
        resultado.config(text="Ingrese el numero valido ")    
    
        # print('An exception ocurred ')
    
# configuracion de lla ventana 
root = tk.Tk() 
root.title("Conversor de temperatura")
root.geometry("300x200") # tamano recomendado

#widgets
tk.Label(root, text="Ingrese temperatura en C:  ").pack(pady = 5)
entry = tk.Entry(root)
entry.pack(pady =5)  # el 5 es la posicion

tk.Button(root, text="Convertir", command=convertir).pack(pady = 5)
resultado = tk.Label(root, text="Resultado: ")
resultado.pack(pady=5)

root.mainloop() 



