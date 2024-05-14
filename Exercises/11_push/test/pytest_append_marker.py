import pytest

def pytest_configure(config):
    config.addinivalue_line("markers","detect_append: mark a test to detect usage of append method")

@pytest.hookimpl(tryfirst=True)
def pytest_pycollect_makeitem(collector,name,obj):
    if collector.funcnamefilter(name) and hasattr(obj, "__annotations__"):
        if "detect_append" in obj.__annotations__:
            item = pytest.Function(name, parent=collector)
            item.obj = obj
            return item