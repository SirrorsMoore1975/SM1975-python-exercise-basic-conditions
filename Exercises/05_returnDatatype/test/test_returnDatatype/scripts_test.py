import pytest
from src.scripts import returnDatatype

@pytest.mask.parametrize("variable,expected",[
    ((1,2,3,4),'tuple'),
    ([1,2,3,4],'list'),
    (5,'number'),
    (True, 'boolean'),
    (1.23, 'float'),
    ("hello",'string'),
    ({"name":"Jeffery"},'dictionary'),
    (range(4), 'range'),
    (None, 'None Type')
])

def test_returnDatatype(variable,expected):
    result = returnDatatype(variable)
    assert result == expected