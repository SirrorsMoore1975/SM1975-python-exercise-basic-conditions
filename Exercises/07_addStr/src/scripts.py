"""
    adding tuple of elements together
"""

def addStr(tuple_args:tuple):
    """
        add tuple of elements together into one string

    Args:
        tuple_args(tuple): tuple contain elements
    Returns:
        returns (str): return a combined string
    """
    result = ""
    for element in tuple_args:
        result += str(element)
    return result
