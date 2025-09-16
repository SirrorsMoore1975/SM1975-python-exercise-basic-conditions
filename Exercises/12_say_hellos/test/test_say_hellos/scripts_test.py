import pytest
from src.scripts import say_hellos
pytest.mark.parametrize('input,expected',[()])
def test_say_hellos(input, expected):
    result=say_hellos(input)
    assert result == expected
