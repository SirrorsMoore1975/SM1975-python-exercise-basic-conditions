import pytest
from src.scripts import addStr

@pytest.mark.parametrize("input,expected",[
    ((1,2,3,4),"1234"),
    (("a","b","c","d","e"), "abcde"),
    (("five"," ", "dollar"), "fivedollar")
])

def test_addStr(input, expected):
    result = addStr(input)
    assert result == expected