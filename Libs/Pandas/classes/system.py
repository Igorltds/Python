import pandas as pd
from os import getcwd


class System():
        def __init__(self):
                self.df = {}


        def df_info(self, file_path):
                self.file_path = file_path
                self.file_name = self.file_path.split('/')[-1]
                self.file_type = self.file_name.split('.')[1]

        def create_df(self, file_path=''):
                self.df_info(file_path)
                match self.file_type:
                        case 'json': self.df = pd.read_json(self.file_path, orient='index')
                        case 'xlsx': self.df = pd.read_excel(self.file_path)
                        case _: print('DEu RUIM')
                
        
        def merge(self, main_df, second_df):
                self.df = main_df.merge(second_df)
        
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

        def add_rows_df(self, new_file_path):
                self.df = pd.concat([self.df, pd.read_excel(new_file_path)], ignore_index=True)
        def add_column_based(self, new_column, base_column):
                # Criar coluna, com base em colunas existentes
                self.df[new_column] = self.df[base_column]*0.05
        def add_column_loc (self, new_column, value):
                # Criar nova coluna, com dados padrões (melhor desempenho parece)
                self.df.loc[:, new_column] = value

        def rm_lines(self, line_id):
                self.df = self.df.drop(id, axis=0)
        def rm_column(self, column):
                self.df = self.df.drop(column, axis=1)
'''
system = System()
print(system.df)

system.create_df('dfs/pandas-json/dataframe.json')

print(system.file_name)
print(system.file_type)'''