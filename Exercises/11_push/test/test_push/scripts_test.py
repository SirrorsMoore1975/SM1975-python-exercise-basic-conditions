import pytest
from src.scripts import push
import inspect

def has_append(func):
    source_lines, _ = inspect.getsourcelines(func)
    source_code = ''.join(source_lines)
    return 'append(' in source_code

def test_push_has_no_append():
    assert has_append(push) is False

@pytest.mark.parametrize("_list, element, expected_list, expected_length",[
    ([1,2,3,4], 5, [1,2,3,4,5], 5),
    ([2,4,6,8], 10, [2,4,6,8,10], 5),
    ([1,3,5,7], 9, [1,3,5,7,9], 5),
    ([1,7,2,4,9], 6, [1,7,2,4,9,6], 6),
    (["a","b","c","d"], "e", ["a","b","c","d","e"], 5),
])

def test_push(_list, element, expected_list, expected_length):
    result = push(_list, element)
    assert _list == expected_list
    assert result == expected_length
