# 1. Clase Banco: Implementa una clase Banco con: Atributo de clase tasa_interes. Método de clase actualizar_tasa(nueva_tasa).  Método calcular_interes(monto) que calcule el interés sobre un monto basado en la tasa actual.
class Banco:
    # Atributo de clase
    tasa_interes = 0.05  # 5% de tasa de interés por defecto

    # Método de clase para actualizar la tasa de interés
    @classmethod
    def actualizar_tasa(cls, nueva_tasa):
        cls.tasa_interes = nueva_tasa
        print(f"Tasa de interés actualizada a: {cls.tasa_interes * 100}%")
    
    # Método para calcular el interés sobre un monto
    def calcular_interes(self, monto):
        interes = monto * self.tasa_interes
        return interes

# Ejemplo de uso
banco = Banco()

# Calcular interés con la tasa por defecto
monto = 1000
interes = banco.calcular_interes(monto)
print(f"Interés sobre {monto}: {interes}")

# Actualizar la tasa de interés
Banco.actualizar_tasa(0.07)  # Nueva tasa de 7%

# Calcular el interés con la nueva tasa
interes = banco.calcular_interes(monto)
print(f"Interés sobre {monto} con nueva tasa: {interes}")
