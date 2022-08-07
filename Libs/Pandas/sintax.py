import pandas as pd
import datetime as dt

def to_date(date):    return dt.datetime.strptime(date, '%Y-%m-%d').date()

def main():
    faturamentos_dict ={"2022-08-04":200.00,
                        "2022-08-05":300.00,
                        "2002-08-06":200.00}
    faturamentos = {'Date':[], 'Value':[]}

    for date, value in faturamentos_dict.items(): 
        faturamentos["Date"].append(to_date(date))
        faturamentos["Value"].append(value)

    print(faturamentos)
    df=pd.DataFrame(faturamentos)
    print(df)


def second(): # Não util
    dict1 ={"0":{"Date":"2022-08-04", "Value":"200.00"},
            "1":{"Date":"2022-08-05", "Value":"300.00"},
            "2":{"Date":"2002-08-06", "Value":"200.00"}}

    df = pd.DataFrame(dict1)
    print(df)

print("\n Iniciado")

main() #primeiro converte datestring para dt.date


