from map import increment, pow2, handler


def test_increment():
    assert increment(10) == 11


def test_pow2():
    assert pow2(5) == 25


def test_handler():
    assert handler(increment, [1, 2, 3]) == [2, 3, 4]
