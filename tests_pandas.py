from Pandas_app.tests.test_01 import Test_01

try:
    test = Test_01('Pandas_app')
    print('\nO Test_01 passou!!! ')
except Exception as inst:
    print('!!! Algo deu Muito errado com o Test_01!!! \n', inst)

finally: print("\nFim do teste de pandas\n")


'''
from Pandas_app.tests.test_02 import Test_02
try:
    if Test_02.main():
        print('\nO Test_02 passou!!! ')
    else: print('!!! Algo deu errado com o Test_02 ')
except: print('!!! Algo deu Muito errado com o Test_02!!! \n')

'''