from Modelo.Model import Tienda
from controllers.Controlador import ControladorTienda
from views.Vista import VistaTienda

if __name__ == "__main__":
    modelo = Tienda()
    modelo.agregar_producto(1,"Manzana", 1000, 100)
    modelo.agregar_producto(2,"Platano", 2.700, 200)
    modelo.agregar_producto(3,"pera", 2.100, 300)

    contolador = ControladorTienda(modelo, None)
    vista = VistaTienda(controlador)
    controlador.vista = vista 



