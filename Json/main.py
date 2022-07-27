#from json import loads, dumps, load, dump


print("\n\nTestando Json")
locale = "Json"

#test_01.py
from app.carro import main1, Carro
main1()

#test_02.py
from app.veiculo import main2, Veiculo
main2(locale)

print("\nFim do teste de Json\n\n")
