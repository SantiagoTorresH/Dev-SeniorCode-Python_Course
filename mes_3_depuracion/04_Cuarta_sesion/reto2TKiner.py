import tkinter as tk
from tkinter import ttk, messagebox
import datetime as datetime


#Variable
clientes = []
mascotas = []

#Clases principales
class SistemaVeterinaria:
    class Persona:
        id_counter = 1
        
        def __init__(self,nombre,contacto):
            self.id = SistemaVeterinaria.Persona.id_counter
            self.nombre = nombre
            self.contacto = contacto
            
            SistemaVeterinaria.Persona.id_counter += 1

    class Cliente(Persona):
        def __init__(self, nombre, contacto,direccion):
            super().__init__(nombre, contacto)
            self.direccion = direccion
            self.mascotas = []
            
        def agregar_mascota(self,mascota):
            self.mascotas.append(mascota)

    class Mascota:
        id_counter = 1
        
        def __init__(self,nombre,especie,raza,edad):
            self.id = SistemaVeterinaria.Mascota.id_counter
            self.nombre = nombre 
            self.especie = especie
            self.raza = raza
            self.edad = edad
            self.historia_clinico= []
            
            SistemaVeterinaria.Mascota.id_counter += 1
            
        def agregar_cita(self,cita):
            self.historia_clinico.append(cita)
            
        def mostar_historial(self):
            return self.historia_clinico
    class Cita:
        id_counter = 1
        
        def __init__(self,fecha,hora,servicio,veterinario):
            self.id = SistemaVeterinaria.Cita.id_counter
            self.fecha = fecha
            self.hora = hora
            self.servicio = servicio
            self.veterinario = veterinario
            
            SistemaVeterinaria.Cita.id_counter += 1


#Funciones auxiliares
def validar_fecha(fecha):
    from datetime import datetime
    try:
        datetime.strptime(fecha,"%Y-%m-%d")
        return True
    except ValueError:
        return False


#Funciones del sistemas
def registrar_cliente(nombre, contacto, direccion ):

    
    cliente = SistemaVeterinaria.Cliente(nombre,contacto,direccion)
    clientes.append(cliente)
    messagebox.showinfo("Exito, ", f"Cliente registrado con exito. ID: {cliente.id} ")
    # print(f"Cliente registrado con exito. ID: {cliente.id}")
    
    
def registrar_mascota(cliente_id, nombre_mascota, especie, raza, edad ):
    
    
    # print("=============REGISTRO DE MASCOTA==========")
    
    # cliente_id = int(input("Ingrese el ID del Cliente para asociar la mascota: "))
    cliente = next((c for c in clientes if c.id == cliente_id), None)
    
    if not cliente:
        messagebox.showerror("Error ", "cliente no encrontrado . ")
        # print("Cliente no encontrado.")
        return
    
    # nombre_mascota= input("Nombre de la mascota: ")
    # especie = input("Especie de la mascota: ")
    # raza = input("Raza de la mascota: ")
    # edad = input("Ingrese edad de la mascota: ")
    
    mascota = SistemaVeterinaria.Mascota(nombre_mascota,especie,raza,edad)
    
    
    cliente.agregar_mascota(mascota)
    mascotas.append(mascota)
    
    messagebox.showinfo("Exito, ", " ")
    print(f"Mascota registrada con exito, ID :{mascota.id}")

def programar_cita():
    
    cliente_id = int(input("Ingrese el ID del cliente: "))
    cliente = next((c for c in clientes if c.id == cliente_id), None)
    
    if not cliente:
        print("Cliente no encontrado.")
        return
    
    mascota_id = int(input("Ingrese el ID del mascota: "))
    mascota = next((m for m in cliente.mascotas if m.id == mascota_id), None)
    
    if not mascota:
        print("Mascota no encontrado.")
        return
    
    fecha = input("Ingrese la fecha de la cita(YYYY-MM-DD): ")
    while not validar_fecha(fecha):
        print("Fecha invalida, Por Favor, use el formato YYYY-MM-DD")
        fecha = input("Ingrese la fecha de la cita(YYYY-MM-DD): ")
    hora = input("Ingrese la hora de la cita (HH:MM): ")
    servicio = input("Ingrese el servicio(Consultoria, vacunacion, etc.): ")
    veterinario = input("Ingrese nombre de Veterinario: ")
    
    cita = SistemaVeterinaria.Cita(fecha,hora,servicio,veterinario)
    mascota.agregar_cita(cita)
    print("Cita agendada")

def consultar_historia():
    
    print("Consultar historial de citas")
    
    cliente_id = int(input("Ingrese el ID del cliente: "))
    cliente = next((c for c in clientes if c.id == cliente_id), None)
    
    if not cliente:
        print("Cliente no encontrado.")
        return
    
    mascota_id = int(input("Ingrese el ID del mascota: "))
    mascota = next((m for m in cliente.mascotas if m.id == mascota_id), None)
    
    if not mascota:
        print("Mascota no encontrado.")
        return

    mascota.mostar_historial()
    
#Menu Principal
#Interfaz de usuario(TKinter)
class VeterinariaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema veterinaria")
        self.root.geometry("500x500")
        
        self.clientes = clientes
        self.mascotas = mascotas
        
        self.main_menu() 
        
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    
        
    def main_menu(self):
        self.clear_window()
        
        tk.Label(self.root, text="Sistema veterinaria", font=("Arial", 16)).pack(pady=5)
        tk.Button(self.root, text="Registrar Cliente", command=self.registrar_cliente).pack(pady=5)  # problems 


        tk.Button(self.root, text="Registrar mascotas", command="").pack(pady=5)
        tk.Button(self.root, text="Registrar cita", command="").pack(pady=5)
        tk.Button(self.root, text="Registrar Historial de citas", command="").pack(pady=5)
        
    def registrar_cliente(self):
        self.clear_window()
        
        tk.Label(self.root, text="Registar clientesa", font=("Arial", 16)).pack(pady=5) 
        
        tk.Label(self.root, text=" Nombre: ").pack(pady=5)
        nombre_entry = tk.Entry(self.root) # el entry es bloque en blanco 
        nombre_entry.pack(pady=5)
        
        tk.Label(self.root, text=" Contacto: ").pack(pady=5)
        contacto_entry = tk.Entry(self.root)
        contacto_entry.pack(pady=5)

        tk.Label(self.root, text=" Direccion: ").pack(pady=5)
        direccion_entry = tk.Entry(self.root)
        direccion_entry.pack(pady=5)                
        
        def submit_cliente():
            nombre = nombre_entry.get()
            contacto = contacto_entry.get()
            direccion = direccion_entry.get()         
            registrar_cliente(nombre, contacto, direccion )    
            self.registrar_mascota() 
                
            
        tk.Button(self.root, text="Registrar Cliente", command=submit_cliente).pack(pady=20)    
        tk.Button(self.root, text="volver al menu principal  ", command=self.main_menu).pack(pady=20)    
        
        
    def registrar_mascota(self):
        self.clear_window()
        
        tk.Label(self.root, text="Registar mascota", font=("Arial", 16)).pack(pady=10)     
        
        tk.Label(self.root, text=" Id Cliente: ").pack(pady=5)
        cliente_id_entry = tk.Entry(self.root)
        cliente_id_entry.pack(pady=5)
        
        tk.Label(self.root, text=" NOmbre Mascota: ").pack(pady=5)
        nombre_mascota_entry = tk.Entry(self.root)
        nombre_mascota_entry.pack(pady=5)
        
        tk.Label(self.root, text=" Especie: ").pack(pady=5)
        especie_combobox = ttk.Combobox(self.root, values=["perro", "gato", "conej", "pajaro", "otros"])
        especie_combobox.pack(pady=5)
        
        tk.Label(self.root, text=" raza : ").pack(pady=5)
        raza_entry = tk.Entry(self.root)
        raza_entry.pack(pady=5)
        
        tk.Label(self.root, text=" Edad: ").pack(pady=5)
        edad_entry = tk.Entry(self.root)
        edad_entry.pack(pady=5)
        
        def submit_mascota():
            cliente_id = int(cliente_id_entry.get())
            nombre_mascota = nombre_mascota_entry.get()
            especie = especie_combobox.get()      
            raza = raza_entry.get()
            edad = int(edad_entry.get())    
            registrar_mascota(cliente_id, nombre_mascota, especie, raza, edad  )    
            self.registrar_mascota() 
                
            
        tk.Button(self.root, text="Registrar Mascota", command=submit_mascota).pack(pady=20)    
        tk.Button(self.root, text="volver al menu principal  ", command=self.main_menu).pack(pady=20)  
            
root = tk.Tk()
app = VeterinariaApp(root)
root.mainloop()          