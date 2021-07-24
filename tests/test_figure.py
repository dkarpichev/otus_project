from collections import namedtuple
import pytest
from src.Basic_Figure import Figure, decimal_integer, pi, sqrt
from src.Square import Square
from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Triangle import Triangle


def create_string_test_data():
    return [
        Square("10", 10),
        Circle("10"),
        Rectangle("10", "12"),
        Triangle(6, "5", 4.3),
    ]


def create_test_area_data():
    return [Square(3), Circle(4), Rectangle(4, 5), Triangle(3, 3, 3)]


def create_test_area():
    return [Square(3)]


def create_error_test_data():
    return [Figure, Square, Circle, Rectangle, Triangle]


@pytest.fixture(scope="function")
def string_square():
    return Square("10")


def compare_objects(assertion_data1, assertion_data2):
    assert (
        assertion_data1 == assertion_data2
    ), f'"{assertion_data1}" != "{assertion_data2}"'


valid_sum_dict = {
    "Square-Square": "18",
    "Square-Circle": "59.265482457436688",
    "Square-Rectangle": "29",
    "Square-Triangle": "12.897114317029974",
    "Circle-Square": "59.265482457436688",
    "Circle-Circle": "100.530964914873376",
    "Circle-Rectangle": "70.265482457436688",
    "Circle-Triangle": "54.162596774466662",
    "Rectangle-Square": "29",
    "Rectangle-Circle": "70.265482457436688",
    "Rectangle-Rectangle": "40",
    "Rectangle-Triangle": "23.897114317029974",
    "Triangle-Square": "12.897114317029974",
    "Triangle-Circle": "54.162596774466662",
    "Triangle-Rectangle": "23.897114317029974",
    "Triangle-Triangle": "7.794228634059948",
}


@pytest.mark.parametrize("test_data", create_string_test_data(), ids=lambda x: x.name)
def test_string_square(test_data):
    if test_data.name == "Square":
        assert test_data.area == 10 ** 2
    elif test_data.name == "Circle":
        assert test_data.area == decimal_integer(pi) * (10 * 10)
    elif test_data.name == "Rectangle":
        assert test_data.area == 10 * 12
    elif test_data.name == "Triangle":
        p = decimal_integer(test_data.perimeter / 2)
        assert test_data.area == decimal_integer(
            (sqrt(p * (p - 6) * (p - 5) * (p - decimal_integer(4.3))))
        )


@pytest.mark.parametrize(
    "test_data", create_error_test_data(), ids=lambda x: x.__name__
)
def test_error_message(test_data):
    if test_data.__name__ == "Figure":
        try:
            test_data(1)
        except Exception as exc:
            assert 'Unable to create class "Figure"' == str(
                exc
            ), 'Unable to create class "Figure"'
    else:
        try:
            test_data(1, 3, 4, 5, 6, 7, 8, 1)
        except Exception as exc:
            if test_data.__name__ == "Circle":
                assert "Use only one value" == str(
                    exc
                ), f"'Use only one value' != {exc}"
            if test_data.__name__ == "Square":
                assert "Use two identical sides or one side" == str(exc), (
                    f"'Use two identical sides or one side' != {exc}" ""
                )
            if test_data.__name__ == "Rectangle":
                assert "Enter the value for the two sides" == str(
                    exc
                ), f"'Enter the value of the two sides' != {exc}"
            if test_data.__name__ == "Triangle":
                assert "NoneType" in str(exc)


@pytest.mark.parametrize("test_data", create_test_area_data(), ids=lambda x: x.name)
@pytest.mark.parametrize("test_data2", create_test_area_data(), ids=lambda x: x.name)
def test_area_sum(test_data, test_data2):
    get_valid_sum = valid_sum_dict[f"{test_data.name}-{test_data2.name}"]
    compare_objects(str(test_data.add_area(test_data2)), get_valid_sum)
