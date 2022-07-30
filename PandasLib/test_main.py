

from classes.test import Test
print('\nIniciando teste')
try: # test
    test = Test()
    test.criar_dfs('dfs/test/')
    test.test()
except Exception as inst:
    print('\n!!! Algo deu Muito errado com o Test!!! \n', inst)
finally: print("\n-----!Teste Iniciado!-----\n")


from tests.teste_vendasgerentes import Test_vendasgerentes
try:
    test = Test_vendasgerentes('dfs/pandas_excel')
    test.criar_dfs_iniciais()
    test.criar_vendasgerentes()
    print(
        f"vendas={test.vendas.get_shape()}",
        f"\ngerentes={test.gerentes.get_shape()}",
        f"\nvendasgerentes: {test.vendasgerentes.get_shape()}")
    
    test.test()

    print('\nO Test_01 passou!!! ')

except Exception as inst:
    print('\n !!!Erro, Teste_vendasgerentes!!!\n', inst)
finally: print("\nFim do test_vendasgerentes.py\n")






'''
from Pandas_app.tests.test_02 import Test_02
try:
    if Test_02.main():
        print('\nO Test_02 passou!!! ')
    else: print('!!! Algo deu errado com o Test_02 ')
except: print('!!! Algo deu Muito errado com o Test_02!!! \n')

'''