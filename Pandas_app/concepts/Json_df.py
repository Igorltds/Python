'''
from json import load
with open("Pandas/concepts/dataframe.json", 'r', encoding='utf-8') as file_json:
    df = pd.DataFrame.from_dict(load(file_json), orient='index')
    print(df)
'''
import pandas as pd
import datetime as dt

df = pd.read_json('Pandas/concepts/dataframe.json', orient='index')
print("\n", df)
print('')

x=0
for data in df['Data']:
    #x=0
    # for id in :
        df['Data'] = pd.to_datetime(data)
        x+=1 


print("--")
print(df['Data'])