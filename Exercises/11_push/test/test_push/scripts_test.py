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
    ([1,7,2,4,9], 6, [1,7,2,4,9,6], 6)
])

def test_push(_list, element, expected_list, expected_length):
    result = push(_list, element)
    assert _list == expected_list
    assert result == expected_length

# def detect_append(script_code):
#     with open(script_code, 'r') as script:
#         codes = script.read()
#     tree = ast.parse(codes)

#     class AppendVisitor(ast.NodeVisitor):
#         def __init__(self):
#             self.has_append = False
        
#         def visit_Call(self, node):
#             if isinstance(node.func, ast.Attribute) and node.func.attr == 'append':
#                 self.has_append = True
#             self.generic_visit(node)
    
#     visitor = AppendVisitor()
#     visitor.visit(tree)

#     return visitor.has_append
    

# @pytest.mark.detect_append
# def test_append_usage():
#     input = [1,2,3,4]
#     result = push(input, 5)
#     assert result == 5
#     assert input == [1,2,3,4,5]

def test01_push():
    input = [1,2,3,4]
    result = push(input, 5)
    assert result == 5
    assert input == [1,2,3,4,5]

def test02_push():
    input = ["a", "b", "c"]
    result = push(input, "d")
    assert result == 4
    assert input == ["a", "b", "c", "d"]


# pytest.mark.parametrize('input,expected',[()])
# def test_push(input, expected):
#     result=push(input)
#     assert result == expected
