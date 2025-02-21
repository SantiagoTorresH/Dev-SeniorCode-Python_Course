import sys 
import os 

# def main(): 
    
#Fijar ruta directa a la logica del negicio (negocio. pu y __init__)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src' ) )) 


from negocio import VendedorBase, VendedorPremium 

import unittest

class TestVendedor(unittest.TestCase):
    def SetUp(self):
        self.vendedor_base = VendedorBase("Luis", 1000)  # comision = 100.0 
        self.vendedor_premium = VendedorPremium("Santi", 2000) # comision = 300.0 
        
        
    def test_calcular_comision_base(self):
        self.asserEqual(self.vendedor_base.calcular_comision(), 100.0)
        
    def test_calcular_comision_premium(self):
        self.asserEqual(self.vendedor_premium.calcular_comision(), 300.0)   
        
        
if __name__ == '__main__':
    unittest.main()           
        
        
        
            






    
