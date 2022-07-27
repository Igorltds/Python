import pandas as pd #install
from IPython.display import display
import openpyxl #install

# Aqui é onde a mágica acontece:
class System():
        def __init__(self):
                self.df = {}
        
        def create_df(self):
                self.df = pd.read_excel(self.locale)
        def add_rows_df(self, locale):
                self.df = pd.concat([self.df, pd.read_excel(locale)], ignore_index=True)
        
        def get_df(self): # retorna o DataFrame
                return(self.df)
        def get_head(self, length=4):
                return self.df.head(length)
        def get_shape(self): #retorna o tamanho do df
                return self.df.shape # SEM args
        def get_describe(self):
                return self.df.describe()
        def get_line_by_id(self, id): # returna uma linha pelo id
                return self.df.loc[id] 
        def get_list_line_by_id(self, list_id): # retorna um df, com linhas dos id especificos
                return self.df.loc[list_id]
        def get_list_line_by_order(self, beginning, end): # retorna um df de id's da ordem
                return self.df.loc[beginning:end]
        def get_item_specify(self, id_linha, name_coluna): # retorna um item específico
                return self.df.loc[id_linha, name_coluna]
        def get_df_filtered_by_column(self, # retorna um df, filtrado por uma coluna
                                        column_name='ID Loja', 
                                        filter_item='Norte Shopping'): 
                return self.df.loc[self.df[column_name]==filter_item]
        def get_columns_of_df_filtered_by_column( #retorna um colunas específicas do df, filtrado por uma coluna
                self, filter_column=0, filter_item=0, list_columns_required=0):
                if (filter_column==0 or filter_item==0)and list_columns_required!=0:
                        df = self.get_df_filtered_by_column()
                        return df.loc[list_columns_required]        
                else:
                        filter_item = self.df[filter_column]==filter_item
                        return self.df.loc[filter_item, list_columns_required]

        def get_specs(self):
                return [self.get_head(2), # printa o começo, arg OPCIONAL
                        self.get_shape(), # printa o tamanho
                        self.get_describe()] # printa a descrição

        def add_column_based(self, new_column, base_column):
                # Criar coluna, com base em colunas existentes
                self.df[new_column] = self.df[base_column]*0.05
        def add_column_loc (self, new_column, value):
                # Criar nova coluna, com dados padrões (melhor desempenho parece)
                self.df.loc[:, new_column] = value
        
        def merge(self, main_df, second_df):
                self.df = main_df.merge(second_df)
        
        def rm_lines(self, line_id):
                self.df = self.df.drop(id, axis=0)
        def rm_column(self, column):
                self.df = self.df.drop(column, axis=1)

class Vendas(System):
        def __init__(self, locale):
                self.locale = locale
                self.df = {}
                self.create_df()
                   
class Gerentes(System):
        def __init__(self, locale):
                self.locale = locale
                self.df = {}
                self.create_df()

class VendasGerentes(System):
        def __init__(self, vendas_df, gerentes_df):
                self.df = {}
                self.merge(vendas_df, gerentes_df)
                
class Interface():
        def __init__(self): pass

        def linha(self, t=10, qtde=0):
                for x in range(0, qtde+1):
                        print(f"{'-'*t}")
        def title(self,var,t=40,qtde1=0,qtde2=0):
                print("")
                self.linha(t, qtde1)
                print(var)
                self.linha(int(t/2), qtde2)        



def instanciar():
        If = Interface()
        vendas   = Vendas(  'Pandas/files/vendas.xlsx')
        gerentes = Gerentes('Pandas/files/gerentes.xlsx')
        vendas_gerentes = VendasGerentes(vendas.get_df(), gerentes.get_df())

        print("\nClasses instanciadas: ",
                "\nvendas:",vendas.get_shape(),
                "\ngerentes: ",gerentes.get_shape(),
                "\nvendas_gerentes: ",vendas_gerentes.get_shape(),
                "\nInstanciamento ocorreu bem. \n")
        return If, vendas_gerentes
If , vendas = instanciar()

# Adicionando dezembro
vendas.add_rows_df('Pandas/files/2019/vendas_dezembro.xlsx') 
print("vendas_gerentes arquivo de dezembro adcionado: ",vendas.get_shape())

# Adicionando Colunas: Comissão e Imposto
vendas.add_column_loc  ('Imposto', 0) # Adcionando coluna com valor padrão
vendas.add_column_based('Comissão', 'Valor Final') # Adcionando coluna com base em outra
print("vendas_gerentes adcionando as colunas 'Imposto' e 'Comissão: ",vendas.get_shape())

#Removendo colunas: Comissão e Imposto
vendas.rm_column('Comissão')
vendas.rm_column('Imposto')
print("vendas_gerentes removendo as colunas 'Imposto' e 'Comissão: ",vendas.get_shape())

