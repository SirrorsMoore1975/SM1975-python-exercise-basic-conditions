import pytest, ast
from src.scripts import isOddWithoutIf

def check_script_without_if(script_code):
    with open(script_code, 'r') as script:
        codes = script.read()
    tree = ast.parse(codes)
    for node in ast.walk(tree):
        if isinstance(node, ast.If):
            return True
    return False

def test_scriptWithoutIf():
    script_path = './../../src/scripts.py'
    result = check_script_without_if(script_path)
    assert result == False

@pytest.mark.parametrize('input,expected',[
    (1, True),
    (2, False),
    (3, True),
    (4, False),
    (16, False),
    (51, True)
])
def test_isOddWithoutIf(input, expected):
    result=isOddWithoutIf(input)
    assert result == expected
