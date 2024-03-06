import pytest
from src.scripts import calculation

@pytest.mark.parametrize("sign, lst, value, expected",[
    ("add",[11,12,13,14,15],5, [16,17,18,19,20]),
    ("add",[-1, 2, -3, 4, -5], 5, [4, 7, 2, 9, 0]),
    ("add",[-1, -2, -3, -4, -5], 5, [4, 3, 2, 1, 0]),
    ("add",[1,2,3,4,5],-5,[-4,-3,-2,-1,0]),
    ("subtract", [11, 12, 13, 14, 15], 10, [1,2,3,4,5]),
    ("subtract", [6,7,8,9,10], 10, [-4, -3, -2, -1, 0]),
    ("subtract", [10,9,8,7,6], -5, [15,14,13,12,11]),
    ("multiply", [1,2,3,4,5], 2, [2,4,6,8,10]),
    ("multiply", [1,2,3,4,5], -2. [-2,-4,-6,-8,-10]),
    ("multiply", [1,5,0,2,4], 3, [3,15,0,6,12]),
])

def test_calculation(sign, lst, value, expected ):
    result = calculation(sign, lst, value)
    assert result == expected