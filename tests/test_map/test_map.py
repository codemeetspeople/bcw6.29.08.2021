import pytest

from map import increment, pow2, handler


@pytest.mark.parametrize('given, expected', [
    (10, 11), (-10, -9), (0, 1)
])
def test_increment(given, expected):
    assert increment(given) == expected


@pytest.mark.parametrize('given, expected', [
    (10, 100), (-10, 100), (0, 0)
])
def test_pow2(given, expected):
    assert pow2(given) == expected


@pytest.mark.parametrize('func', [
    (increment,), (pow2,)
])
def test_functions_raise_exception(func):
    with pytest.raises(TypeError):
        func('string value')


@pytest.mark.parametrize('func, array, expected', [
    (increment, [1, 2, 3, 4, 5], [2, 3, 4, 5, 6]),
    (pow2, [1, 2, 3, 4, 5], [1, 4, 9, 16, 25])
])
def test_handler(func, array, expected):
    assert handler(func, array) == expected
