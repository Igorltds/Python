from Pandas_app.vendas import System, Vendas, VendasGerentes, Gerentes

class Test_01():
    def __init__(self, path=''):
        self.vendas = ''
        self.path = path
        self.instanciar()
        self.test()
        print('foi mesmo')

    def instanciar(self):
            vendas   = Vendas(  f'{self.path}/files/vendas.xlsx')
            gerentes = Gerentes(f'{self.path}/files/gerentes.xlsx')
            self.vendas = VendasGerentes(vendas.get_df(), gerentes.get_df())
            print("\nClasses instanciadas: ",
                    "\nvendas:",vendas.get_shape(),
                    "\ngerentes: ",gerentes.get_shape(),
                    "\nvendas_gerentes: ",self.vendas.get_shape(),
                    "\nInstanciamento ocorreu bem. \n")
    def test(self):
        # Adicionando dezembro
        self.vendas.add_rows_df(f'{self.path}/files/2019/vendas_dezembro.xlsx') 
        print("vendas_gerentes arquivo de dezembro adcionado: ",self.vendas.get_shape())

        # Adicionando Colunas: Comissão e Imposto
        self.vendas.add_column_loc  ('Imposto', 0) # Adcionando coluna com valor padrão
        self.vendas.add_column_based('Comissão', 'Valor Final') # Adcionando coluna com base em outra
        print("vendas_gerentes adcionando as colunas 'Imposto' e 'Comissão: ",self.vendas.get_shape())

        #Removendo colunas: Comissão e Imposto
        self.vendas.rm_column('Comissão')
        self.vendas.rm_column('Imposto')
        print("vendas_gerentes removendo as colunas 'Imposto' e 'Comissão: ",self.vendas.get_shape())
