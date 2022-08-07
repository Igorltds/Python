

from classes.test import Test
print('\nIniciando teste')
try: # test
    if Test().main()['test_01'] == True: print('Normalmente')

    else: print('!!!!ERRO!!!!')
except Exception as inst:   
    print('\n!!! Algo deu Muito errado com o Test!!! \n', inst)
finally: print("\n-----!Teste Iniciado!-----\n")


from tests.test_vendasgerentes import Test_vendasgerentes
try:
    if Test_vendasgerentes('dfs/pandas_excel').main() == True: print('teste_vendas gerentes correu bem')

    else: print('!!!!ERRO!!!!')
except Exception as inst:   
    print('\n!!! Algo errado: teste_vendasgerentes !!!\n', inst)


'''
from tests.test_json import Test_json
try:
    if Test_json.main():
        print('\nO Test_02 passou!!! ')
    else: print('!!! Algo deu errado com o Test_02 ')
except: print('!!! Algo deu Muito errado com o Test_02!!! \n')
'''
