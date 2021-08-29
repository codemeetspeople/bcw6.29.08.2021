import pytest

from generators import ari_prog


@pytest.mark.parametrize('generator, expected_values', [
    (ari_prog(0, 5), [0, 1, 2, 3, 4]),
    (ari_prog(0, 10, 2), [0, 2, 4, 6, 8])
])
def test_ari_prog(generator, expected_values):
    for value in expected_values:
        assert next(generator) == value

    with pytest.raises(StopIteration):
        next(generator)
