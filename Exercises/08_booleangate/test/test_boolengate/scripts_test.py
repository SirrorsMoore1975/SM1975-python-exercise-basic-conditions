import pytest
from src.scripts import booleangate, booleangate_not, giveTrue, inverse_True

def test_giveTrue():
    assert giveTrue() == True

@pytest.mark.parametrize("input,expected",[
    ([], True),
    ({}, True),
    (10,False),
    ([1,2,3],False),
    ({"user":"John", "age":20,"gender":"male"},False)
])

def test_inverseTrue(input,expected):
    result = inverse_True(input)
    assert result == expected

@pytest.mark.parametrize("input, expected",[
    (giveTrue(), False),
    (True, False),
    (not giveTrue(),True),
    (True == True, False),
    (True and True, False),
    (True > False, False),
    (True == False, True),
    ({},True),
    ([],True),
    ({} == {}, False),
    ([] == [], False),
    ({} == [], True),
    (inverse_True(1), True),
    (inverse_True(0), False)

])

def test_booleangate_not(input, expected):
    result=booleangate_not(input)
    assert result == expected

@pytest.mark.parametrize("logic, x, y, expected",
[
    ("and",False,False,False),
    ("and",False,True,False),
    ("and",True,False,False),
    ("and",True,True,True),
    ("and","","bananas",""),
    ("and","bananas","",""),
    ("and","",True,""),
    ("and","",False,""),
    ("and","bananas",True,True),
    ("and","bananas",False,False),
    ("and",True,"",""),
    ("and",False,"",False),
    ("and",True,"bananas","bananas"),
    ("and",False,"bananas",False),
    ("and",0,1,0),
    ("and",1,0,0),
    ("and",0,1,0),
    ("and",1,1,1),
    ("and",{},{"a":1},{}),
    ("or",True, True, True),
    ("or",True, False, True),
    ("or",False, True, True),
    ("or",False, False, False),
    ("or","", False, False),
    ("or",False, "", ""),
    ("or","", True, True),
    ("or",True, "", True),
    ("or","", "bananas", "bananas"),
    ("or","bananas", "", "bananas"),
    ("or","bananas", True, "bananas"),
    ("or","bananas", False, "bananas"),
    ("or",True, "bananas", True),
    ("or",False, "bananas", "bananas"),
    ("or","", "", ""),
    ("or","bananas", "bananas", "bananas"),
    ("or","apples", "bananas", "apples"),
    ("or","abcd", "efgh", "abcd"),
    ("or",0,0,0),
    ("or",1,3,1),
    ("or",0,4,4),
    ("or",6,0,6),
]
)

def test_booleangate(logic,x,y,expected):
    result = booleangate(logic, x, y)
    assert result == expected