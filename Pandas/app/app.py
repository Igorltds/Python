import pandas as pd #install
from IPython.display import display
import openpyxl #install

# Aqui é onde a mágica acontece:
class Vendas():
        def __init__(self, ano):
                self.locale = ano
                self.vendas = { 'setembro':'',
                                'dezembro':''}
                self.create_df('setembro')
                self.create_df('dezembro')

        def create_df(self, mes):
                self.vendas[mes] = pd.read_excel(f"{self.locale}Vendas_{mes}.xlsx")
                print(f"\n{mes} criado!\n")
        def all_display_df (self, mes, t=10):
                match mes: # definindo mês do df
                        case 'setembro':
                                df = self.vendas['setembro']
                        case 'dezembro':
                                df = self.vendas['dezembro']
                
                If.title(f"  Display specs of DataFrame of {mes}: ",40, 1, 0) 
                
                # Começo
                If.title("head(): ", t, 0, -1)
                display(df.head()) # arg opcional
                # Tamanho
                If.title("shape: ", t, 0, -1)
                display(df.shape) # SEM arg
                # Descrição
                If.title("describe(): ", t, 0, -1)
                display(df.describe())


                If.title("loc(): ", t, 0, -1)

                # Sob condição de um id
                display(df.loc[5])
                If.linha()
                # Sob condição de uma lista de id's
                display(df.loc[[0,1]]) 
                If.linha()
                # Sob condição de uma lista ordenada de id's
                display(df.loc[0:5]) 
                If.linha()
                # item específico
                display(df.loc[5, 'ID Loja'])
                If.linha()
                # Sob condição de conteudo(linha) de uma coluna
                vendas_norte_shopping_df = df.loc[df['ID Loja']=='Norte Shopping']
                display(vendas_norte_shopping_df) 
                If.linha()
                # Sob condição de conteudo de uma coluna, apenas algumas colunas retornam
                linhas = df['ID Loja']=='Norte Shopping'
                colunas = ['ID Loja', 'Produto', 'Quantidade']
                vendas_norte_shopping_df =  df.loc[linhas, colunas]
                display(vendas_norte_shopping_df)
                If.linha()
        def edit(self, mes):
                # Criar coluna, com base em colunas existentes
                vendas_df['comissão'] = vendas_df['Valor Final']*0.05

                # Criar nova coluna, com dados padrões (melhor desempenho parece)
                vendas_df.loc[:, 'imposto'] = 0
                display(vendas_df)

# para um teste de mesa menos poluido:
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


# Instanciando Vendas e Interface
vendas_2019 = Vendas('app/')
If = Interface()

# Printar os dois relatorios dos respectivos meses: 
vendas_2019.all_display_df('setembro')
vendas_2019.all_display_df('dezembro')

