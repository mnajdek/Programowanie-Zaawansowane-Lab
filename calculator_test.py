from calculator import Calculator
import numpy as np
import pytest

@pytest.fixture(scope="function")
def calc(request):
    c = Calculator()
    return c

class TestCalc:
    @pytest.mark.parametrize(
        "a,b,exp", [(1, 1, 2), (0, 3, 3), ([1, 2, 3], [2, 2, 2], [3, 4, 5])]
    )
    def test_add(self, calc, a, b, exp):
        result = calc.add(a, b) == exp
        if isinstance(result, np.ndarray):
            assert result.all()
        else:
            assert result

    @pytest.mark.parametrize(
        "a,b,exp", [(1, 1, 0), (0, 3, -3), ([1, 2, 3], [2, 2, 2], [-1, 0, 1])]
    )
    def test_sub(self, calc, a, b, exp):
        result = calc.substract(a, b) == exp
        if isinstance(result, np.ndarray):
            assert result.all()
        else:
            assert result

    @pytest.mark.parametrize(
        "a,b,exp", [(1, 1, 1), (0, 3, 0), ([1, 2, 3], [2, 2, 2], [2, 4, 6])]
    )
    def test_mul(self, calc, a, b, exp):
        result = calc.multiply(a, b) == exp
        if isinstance(result, np.ndarray):
            assert result.all()
        else:
            assert result

    @pytest.mark.parametrize(
        "a,b,exp",
        [
            (1, 0, 1),
            (1, 1, 1),
            (0, 3, 0),
            ([1, 2, 3], [2, 2, 2], [0.5, 1, 3 / 2]),
        ],
    )
    def test_div(self, calc, a, b, exp):
        result = calc.divide(a, b) == exp
        if isinstance(result, np.ndarray):
            assert result.all()
        else:
            assert result

    @pytest.mark.parametrize(
        "a,exp",
        [(4, 2), (9, 3), ([4, 9, 16], [2, 3, 4])],
    )
    def test_sqrt(self, calc, a, exp):
        result = calc.sqrt(a) == exp
        if isinstance(result, np.ndarray):
            assert result.all()
        else:
            assert result

test=TestCalc()
print(test.test_add)
print(test.test_sub)
print(test.test_mul)
print(test.test_div)
print(test.test_sqrt)
