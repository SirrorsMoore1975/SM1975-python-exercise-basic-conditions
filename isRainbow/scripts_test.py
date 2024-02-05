import pytest
from scripts import isRainbowColor

@pytest.mark.parametrize("color,expected",[
    ("red",True),
    ("rED",True),
    ("Brown", False),
    ("Yellow", True),
    ("Violet", True),
    ("Black", False),
    ("Blue", True),

])

def test_isRainbow(color,expected):
    assert isRainbowColor(color) == expected