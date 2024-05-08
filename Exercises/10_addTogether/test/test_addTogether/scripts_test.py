import pytest
from src.scripts import addTogether

@pytest.mark.parametrize("x,y,expected",[
    ([1,2,3],[4,5,6],[5,7,9]),
    ([1,2,3],[7,8,9],[8, 10, 12])
    
])

def test_addTogether(x,y,expected):
    result = addTogether(x,y)
    assert result == expected

# Advanced: alter addTogether so it also pass the following test
@pytest.mark.parametrize("x,y,expected",[
    ([1],[4,5,6],[5,5,6]),
    ([1,5,6],[4],[5,5,6])
])
def test_addTogether_Advanced(x,y,expected):
    result = addTogether(x,y)
    assert result == expected

# Intermediate: alter addTogether so that it can take multiple list and add them together
@pytest.mark.parametrize("x, expected",[
    (([1,2,3],[4,5,6]), [5,7,9]),
    (([1,2,3],[7,8,9]), [8, 10, 12]),
    (([1],[4,5,6]), [5,5,6]),
    (([1,5,6],[4]), [5,5,6]),
    (([1],[4,5,6],[2,3,4]), [7,8,10]),
    (([4,5,6],[1,3,4],[2]), [7,8,10]),
    (([1, 2, 3], [4, 5], [6]), [11, 7, 3]),
    (([],[]),[0]),
    (([],[0,0],[0,0,0]),[0,0,0]),
    (([],[],[1,2,3]),[1,2,3])
])

def test_addTogether_Intermediate(x, expected):
    
    result = addTogether(*x)
    assert result == expected