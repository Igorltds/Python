'''
from json import load
with open("Pandas_app/files/dataframe.json", 'r', encoding='utf-8') as file_json:
    df = pd.DataFrame.from_dict(load(file_json), orient='index')
    print(df)
'''
import pandas as pd
import datetime as dt
import json
from Pandas_app.vendas import System

class Json_pandas(System):
    def main(self):
        pass
        
        

try:
    df = pd.read_json('Pandas_app/files/dataframe.json', orient='index')
    print("\n", df)
    print('')

    #convertendo coluna de string de data para objeto datetime
    df['Data'] = pd.to_datetime(df['Data'])

except Exception as ERRo:
    with open("Pandas_app/concepts/dataframe.json", 'w', encoding='utf-8') as json_file:
        json.dump(df.to_json(orient='index'), json_file)

    print("--")

finallly: print(df)