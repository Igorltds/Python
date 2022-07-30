print("\n\nTestando Json")

locale = "Json"

# test_01.py
from Json_app.carro import Carro

try: 
    main = Carro("honda", "hrv", "prata")
    value = True
except: value = False
finally: print(f'test_01 json: {value}')


# test_02.py
from Json_app.veiculo import Veiculo

try:
    veiculos = Veiculo('Json_app/files') # Instanciando

    veiculos.add_cars(
        {"00000004": ["honda","hrv", "prata"], # Add cars'
        "00000005": ["test0", "tes", "test0"],
        "00000006": ["test0", "tes", "test0"]}
        )

    veiculos.update_json() # SaveFile
except: value = False
finally: print(f'test_02 json: {value}')

print("\nFim do teste de Json\n")