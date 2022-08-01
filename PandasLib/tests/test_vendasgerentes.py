from classes.test import Test
from classes.pandas_excel_vendas import Vendas, Gerentes, VendasGerentes

class Test_vendasgerentes(Test):
    def __init__(self, dfs_path):
        self.dfs_path = dfs_path
        self.vendas   = Vendas()
        self.gerentes = Gerentes()
    def main(self):
        self.criar_dfs_iniciais()
        self.criar_vendasgerentes()
        # print(
        # f"vendas={self.vendas.get_shape()}",
        # f"\ngerentes={self.gerentes.get_shape()}",
        # f"\nvendasgerentes: {self.vendasgerentes.get_shape()}")
        self.test()
        print('final_shape_vendas gerentes: ', self.vendasgerentes.get_shape(), )
        return True

    def criar_dfs_iniciais(self):
        self.vendas.create_df(f'{self.dfs_path}/vendas.xlsx')
        self.gerentes.create_df(f'{self.dfs_path}/gerentes.xlsx')
        

    def criar_vendasgerentes(self):
        self.vendasgerentes = VendasGerentes(self.vendas.get_df(), self.gerentes.get_df())
        self.vendasgerentes.create_df()
        
        
    def test(self):
        # Adicionando dezembro
        self.vendasgerentes.add_rows_df(self.dfs_path+'/past_months/vendas_dezembro.xlsx') 
        #print("vendas_gerentes arquivo de dezembro adcionado: ",self.vendasgerentes.get_shape())

        # Adicionando Colunas: Comissão e Imposto
        self.vendasgerentes.add_column_loc  ('Imposto', 0) # Adcionando coluna com valor padrão
        self.vendasgerentes.add_column_based('Comissão', 'Valor Final') # Adcionando coluna com base em outra
        #print("vendas_gerentes adcionando as colunas 'Imposto' e 'Comissão: ",self.vendasgerentes.get_shape())

        #Removendo colunas: Comissão e Imposto
        self.vendasgerentes.rm_column('Comissão')
        self.vendasgerentes.rm_column('Imposto')
        #print("vendas_gerentes removendo as colunas 'Imposto' e 'Comissão: ",self.vendasgerentes.get_shape())
