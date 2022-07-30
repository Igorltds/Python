import openpyxl 
import pandas as pd
from classes.system import System

class Vendas(System):
        def __init__(self):
                pass
                
class Gerentes(System):
        def __init__(self):
                pass

class VendasGerentes(System):
        def __init__(self, vendas_df, gerentes_df):
                self.vendas_df = vendas_df
                self.gerentes_df = gerentes_df
        
        def create_df(self):
                self.merge(self.vendas_df, self.gerentes_df)
        
