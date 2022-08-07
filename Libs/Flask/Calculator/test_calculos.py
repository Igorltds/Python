from calculos import Soma, Subtração, Multiplicação, Divisão
from interface import Frames
class Test_calculos():

    def soma(a, b):
        print(f"Soma \nResultado: {Soma.soma(a, b)}")
        print("------------------------")
    
    def subtração(a, b):
        print(f"Subtração \nResultado: {Subtração.Subtrai(a, b)}")
        print("------------------------")

    def multiplicação(a, b):
        print(f"Multiplicação \nResultado: {Multiplicação.multiplica(a, b)}")
        print("------------------------")

    def divisão(a, b):
        print(f"Divisão \nResultado: {Divisão.divide(a, b)}")
        print("------------------------")

#------------------------------------------------------------

Frames.print_title("test_calculos.py")

Frames.print_subtitle("Numeros Certos")
Test_calculos.soma(1, 5)
Test_calculos.subtração(1, 7)
Test_calculos.multiplicação(2, 3)
Test_calculos.divisão(12, 2)

Frames.print_subtitle("strings")
Test_calculos.soma(1, "5")
Test_calculos.subtração(1.0, "7.0")
Test_calculos.multiplicação("2", 3.0)
Test_calculos.divisão(12.0, "2")
