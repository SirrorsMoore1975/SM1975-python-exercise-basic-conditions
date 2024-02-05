import pytest
from scripts import flatten

@pytest.mark.parametrize("_list, expected",[
    ([1, 2, 3, [4, 5, 6]],[1, 2, 3, 4, 5, 6]),
    ([[1, 2, 3],[4, 5, 6],],[1, 2, 3, 4, 5, 6]),
    ([[1], [2], [3], [4, 5, 6]],[1, 2, 3, 4, 5, 6]),
    ([
        [9, 3, 8, 3],
        [4, 5, 2, 8],
        [6, 4, 3, 1],
        [1, 0, 4, 5],
    ],[9, 3, 8, 3, 4, 5, 2, 8, 6, 4, 3, 1, 1, 0, 4, 5]),
    ([[1, 2, 3], [3, 6, 7], [7, 5, 4], 7],[1, 2, 3, 3, 6, 7, 7, 5, 4, 7])
])

def test_flatten(_list,expected):
    assert flatten(_list) == expected