from sys import path
path.insert(1,'/home/luaa/projects/python/tests/geometric_figures')

import pytest 
from src.triangle import triangle


def test_equilateral_triangle():
    assert triangle(5,5,5) == "equilateral_triangle"

def test_isoceles_triangle():
    assert triangle(5,5,4) == "isoceles_triangle"

def test_scalene_triangle():
    assert triangle(2,5,4) == "scalene_triangle"

def test_it_is_not_triangle():
    assert triangle(0,5,4) == "it_is_not_triangle"

#não sei oq é isso.. dá como "passed"
'''
def test_triangle_typError():
    with pytest.raises(TypeError):
        triangle(2,5,'4')
'''
