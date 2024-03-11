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
    ("multiply", [1,2,3,4,5], -2, [-2,-4,-6,-8,-10]),
    ("multiply", [1,5,0,2,4], 3, [3,15,0,6,12]),
    ("divide", [10,8,6,4,2], 2, [5,4,3,2,1]),
    ("divide", [0, 0 , 100], 0, [0,0,0]),
    ("divide", [100,100,100],0,[0,0,0]),
    ("getRemainder", [1,2,3,4], 2, [1,0,1,0]),
    ("getRemainder", [2,4,6,8], 2, [0,0,0,0]),
    ("getRemainder", [1,2,3,4,5,6,7,8,9], 3, [1,2,0,1,2,0,1,2,0]),
])

def test_calculation(sign, lst, value, expected ):
    result = calculation(sign, lst, value)
    assert result == expected