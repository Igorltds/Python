from test_01 import Test_01
try:
    if Test_01.main():
        print('\nO Test_01 passou!!! ')
    else: print('!!! Algo deu errado com o Test_01 ')
except: print('!!! Algo deu Muito errado com o Test_01!!! \n')


from test_02 import Test_02
try:
    if Test_02.main():
        print('\nO Test_02 passou!!! ')
    else: print('!!! Algo deu errado com o Test_02 ')
except: print('!!! Algo deu Muito errado com o Test_02!!! \n')

