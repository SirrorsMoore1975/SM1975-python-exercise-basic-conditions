import pytest
from src.scripts import push


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
    

@pytest.mark.detect_append
def test_append_usage():
    input = [1,2,3,4]
    result = push(input, 5)
    assert result == 5
    assert input == [1,2,3,4,5]

    


# pytest.mark.parametrize('input,expected',[()])
# def test_push(input, expected):
#     result=push(input)
#     assert result == expected
