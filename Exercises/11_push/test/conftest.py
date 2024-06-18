# import ast
# import pytest

# def detect_append_usage(script):
#     tree = ast.parse(script)

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

# @pytest.hookimpl(tryfirst=True)
# def pytest_runtest_protocol(item, nextitem):
#     marker = item.get_closest_marker("detect_append")
#     if marker:
#         function_source = item.obj.__code__
#         with open(function_source.co_filename, "r") as file:
#             script = file.read()

#         if detect_append_usage(script):
#             pytest.fail("The function uses the append method", pytrace=False)

#     return None

# pytest_plugins = ["pytest_append_marker"]