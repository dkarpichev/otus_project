from collections import namedtuple
import pytest
from src.Basic_Figure import Figure, decimal_integer, pi,sqrt
from src.Square import Square
from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Triangle import Triangle



def create_string_test_data():
    return [Square('10', 10), Circle('10'),Rectangle('10','12'),Triangle(6, '5', 4.3)]

@pytest.fixture(scope='function')
def string_square():
    return Square('10')

@pytest.mark.parametrize("test_data", create_string_test_data(), ids=lambda x: x.name)
def test_strung_square(test_data):
    if test_data.name == 'Square':
        assert test_data.area == 10**2
    elif test_data.name == 'Circle':
        assert test_data.area == decimal_integer(pi)*(10*10)
    elif test_data.name == 'Rectangle':
        assert test_data.area == 10*12
    elif test_data.name == 'Triangle':
        p = decimal_integer(test_data.perimeter / 2)
        assert test_data.area == decimal_integer((sqrt(p*(p-6)*(p-5)*(p-decimal_integer(4.3)))))
    else:
        raise Exception("asdfgt")
