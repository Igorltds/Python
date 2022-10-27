from unittest import TestCase, main as test_main


from geometria import Circulo
class test_Circulo(TestCase):
    

    def test_circulo_verm(self):
        cverm = Circulo("vermelho", 5)
        self.assertEqual(cverm.cor, "vermelho")
        self.assertEqual(cverm.raio, 5)
        self.assertEqual(cverm.calcular_area(), 78.54)

    def test_circulo_azul(self):
        cazul = Circulo("azul", 7)
        self.assertEqual(cazul.cor, "azul")
        self.assertEqual(cazul.raio, 7)
        self.assertEqual(cazul.calcular_area(), 153.94)

    def test_circulo_amar(self):
        camar = Circulo("amarelo", 9)
        self.assertEqual(camar.cor, "amarelo")
        self.assertEqual(camar.raio, 9)
        self.assertEqual(camar.calcular_area(), 254.47)




from geometria import Quadrado
class test_Quadrado(TestCase):


    def test_quadrado_verm(self):
        qverm = Quadrado("vermelho", 10)
        self.assertEqual(qverm.cor, "vermelho")
        self.assertEqual(qverm.lado, 10)
        self.assertEqual(qverm.calcular_area(), 100)


    def test_quadrado_azul(self):
        qazul = Quadrado("azul", 14)
        self.assertEqual(qazul.cor, "azul")
        self.assertEqual(qazul.lado, 14)
        self.assertEqual(qazul.calcular_area(), 196)


    def test_quadrado_amar(self):
        qamar = Quadrado("amarelo", 18)
        self.assertEqual(qamar.cor, "amarelo")
        self.assertEqual(qamar.lado, 18)
        self.assertEqual(qamar.calcular_area(), 324)


from geometria import Triangulo
class test_Triangulo(TestCase):

    def test_triangulo_verm(self):
        tverm = Triangulo("vermelho", 10, 5)
        self.assertEqual(tverm.cor, "vermelho")
        self.assertEqual(tverm.altura, 10)
        self.assertEqual(tverm.base, 5)
        self.assertEqual(tverm.calcular_area(), 25)



# python -m unittest -v
if __name__ == "__name__" :
    test_main()

