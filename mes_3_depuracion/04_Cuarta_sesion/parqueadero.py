import tkinter as tk
from tkinter import ttk, messagebox
import datetime

class Vehiculo:
    def __init__(self, placa, hora_entrada):
        self.placa = placa
        self.hora_entrada = hora_entrada
        
    def calcular_tiempo(self):
        hora_salida = datetime.datetime.now()
        print(hora_salida)
        tiempo_total = hora_salida - self.hora_entrada
        return tiempo_total.total_seconds() / 60
class parqueaderoApp:
    def __init__(self, root):
        self.root.title("Control de parqueadero")
        self.root.geometry("500x400")
        
        self.vehiculos = { }
        
        # Entrada de la placa
        tk.Label(root, text="Placa del vehiculo: ").pack(pady= 5)
        self.entry_placa = tk.Entry(root) #Entry para la caja de texto
        self.entry_placa.pack(pady=5)
        
        #Botones
        tk.Button(root, text= "Registro entrada", command = self.registro_entraeda).pack(pady=5)
        tk.Button(root, text= "Registro salida", command="").pack(pady=5)
        
        #tabla de vehiculos
        self.tree = ttk.Treview(root, columns=("placa","HOra de entrada" ), show="headings")
        self.treeheading("placa", text="placa")
        self.treeheading("hora de entrada", text="hora de entrada")
        self.tree.pack(pady=5, fill="both", expand = True) 
        
    def registro_entrada(self):
        placa = self.entry_placa.get().upper()
        print(placa) 
        if placa and placa not in self.vehiculos:
            hora_actual = datetime.datetime.now().strftime("%H:%M:%s")
            # print(hora_actual)
            self.vehiculos[placa] = Vehiculo(placa, datetime.datetime.now() )
            # print(self.vehiculos)
            self.tree.insert("", "end", iid=placa, values = (placa, hora_actual))
            
    def registrar_salida(self):
        placa = self.entry_placa.get().upper()
        if placa in self.vehiculos:
            Vehiculo = self.vehiculos.pop(placa) 
            tiempo_parque = Vehiculo.calcular_tiempo()
            
            #eliminar de la tabla
            self.tree.delete(placa)
            
            messagebox.showinfo("salida", f"vehiculo {placa} salio. \nTiempo: {tiempo_parque:.2f} minutos")
        else:
            messagebox.showerror("Error", "vehiculo no encontrado")    
            
        # print("tiempo_parque")
        
root = tk.Tk()
app = parqueaderoApp(root)
root.mainloop()            




