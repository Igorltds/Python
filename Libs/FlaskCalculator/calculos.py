class Soma():
    def soma(a, b):
        try: return a+b
        except: return "erro na soma simples"


class Subtração():
    def Subtrai(a, b):
        try: return a-b
        except: return "erro na subtração simples"


class Multiplicação():
    def multiplica(a, b):
        try: return a*b
        except: return "erro na multiplicação simples"


class Divisão():
    def divide(a, b):
        try: return a/b
        except: return "erro na divisão simples"


class Potenciação():
    def potencia(v1,v2):
        try:
            return v1**v2
        except:
            return "digitos inválidos para potenciação"


class Raiz():
    def raiz(v1, v2):
        try: 
            return v1**1/v2
        except:
            return "digitos inválidos para raiz. "


class Logaritimo():
    def logaritimo(v1,v2):
        try:
            return log(v1, v2)
        except:
            return "digitos invalidos para o logaritimo"

