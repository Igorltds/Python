from sys import path
path.insert(1,'/home/luaa/projects/python/tests/geometric_figures')

from src.circle import Circle
import pytest

@pytest.fixture
def circle():
    circle = Circle(2, 3)
    return circle

#test-attributes
def test_circle_radius(circle):
    assert circle.get_radius()==2
def test_circle_height(circle):
    assert circle.get_height()==3

#test_methodes
def test_area_return_radius(circle):
    assert circle.calculate_area() == 12.56
def test_area_return_volume(circle):
    assert circle.calculate_volume() == 37.68
