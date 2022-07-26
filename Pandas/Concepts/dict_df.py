import pandas as pd #install
from IPython.display import display
import openpyxl #install


def dict_df(): # dict dataframe
        vendas={'data': ['15/02/2021', '16/02/2021'],
                'valor': [500, 300],
                'produto': ['feijao', 'arroz'],
                'qtde': [50, 70],
               }
        vendas_df = pd.DataFrame(vendas)
        return vendas_df
display(dict_df())