import pytest
from src.scripts import getTimeOfDay

@pytest.mark.parametrize("hours,minutes,meridiem,expected",[
    (0,31,"AM","invalid input"),
    (3,29,"AM","night"),
    (3,59,"AM","night"),
    (4,0,"AM","morning"),
    (4,30,"AM","morning"),
    (11,59,"AM","morning"),
    (12,0,"PM","afternoon"),
    (4,59,"PM","afternoon"),
    (5,30,"PM","evening"),
    (8,29,"PM","evening"),
    (8,30,"PM","night"),
    (11,59,"PM","night"),
    (12,0,"AM","night"),
    (12,59,"AM","night")
])

def test_getTimeOfDay(hours:int,minutes:int,meridiem:str,expected:str):
    assert getTimeOfDay(hours,minutes,meridiem) == expected