from abc import abstractmethod, ABC
from math import pi 

class Figura(ABC):
  
    def __init__(self, cor:str) -> None:
        self.__cor = cor
    
    @property
    def cor(self) -> str:  return self.__cor
    @cor.setter
    def cor(self, value:str) -> None: self.__cor = value

    @abstractmethod
    def calcular_area(self) -> float: pass


class Circulo(Figura):

    def __init__(self, cor:str, raio:float) -> None:
        super().__init__(cor)
        self.__raio = raio
    
    @property
    def raio(self) -> float: return self.__raio
    @raio.setter
    def raio(self, value:float) -> None: self.__raio = value

    def calcular_area(self) -> float: return round((pi * (self.__raio ** 2)), 2)


class Quadrado(Figura):

    def __init__(self, cor:str, lado:float) -> None:
        super().__init__(cor)
        self.__lado = lado 

    @property
    def lado(self) -> float: return self.__lado
    @lado.setter
    def lado(self, value:float) -> None: self.__lado = value

    def calcular_area(self) -> float: return  self.__lado** 2

class Triangulo(Figura):

    def __init__(self, cor:str, altura:float, base:float) -> None:
        super().__init__(cor)
        self.__altura = altura
        self.__base = base

    @property
    def altura(self) -> float: return self.__altura
    @altura.setter
    def altura(self, value:float) -> None: self.__altura = value

    @property
    def base(self) -> float: return self.__base
    @base.setter
    def base(self, value:float) -> None: self.__base = value

    def calcular_area(self) -> float: return (self.__base*self.__altura)/2
        

