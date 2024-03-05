import pytest
from src.scripts import calculation

@pytest.mark.parametrize("sign, list, value, expected",[
    ("add",[11,12,13,14,15],5, [16,17,18,19,20]),
    ("add",[-1, 2, -3, 4, -5], 5, [4, 7, 2, 9, 0]),
    ("add",[-1, -2, -3, -4, -5], 5, [4, 3, 2, 1, 0]),
    ("add",[1,2,3,4,5],-5,[-4,-3,-2,-1,0]),
    ("subtract", [11, 12, 13, 14, 15], 10, [1,2,3,4,5]),
    ("subtract", [6,7,8,9,10], 10, [-4, -3, -2, -1, 0]),
])