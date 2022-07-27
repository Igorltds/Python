'''
from json import load
with open("Pandas/concepts/dataframe.json", 'r', encoding='utf-8') as file_json:
    df = pd.DataFrame.from_dict(load(file_json), orient='index')
    print(df)
'''
import pandas as pd

df = pd.read_json('Pandas/concepts/dataframe.json', orient='index')
print(df)
