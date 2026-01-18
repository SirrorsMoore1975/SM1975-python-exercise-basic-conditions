"""
booleangate_not\n
@param {expression} ??? the input conditional operand expression that expecting boolean \n
@returns {any} ??? return inverse of the input boolean\n

boolengate
@param {"and|or|nand|nor"} ??? the logic gate expected the output to behave according to input 
@param {expression} ??? the first operand expression
@param {expression} ??? the second operand expression
@returns {any} ??? the expression expected depends on the logic gate 
"""

def booleangate_not(A : bool) -> bool:
    """
        Inverse the input boolean

    Args:
        A (bool): boolean that wanted to be NOT of 
    Returns:
        return (bool): NOT of A
    """
    if isinstance(A, bool):
        return not A
    raise ValueError("input not boolean")

def booleangate(logic: str, X:bool, Y:bool)-> bool:
    """
        Provide output depends on logic and its input
    
    Args:
        logic (str): logic's name
        X (bool): the supposed boolean
        Y (bool): the second supposed boolean
    Returns:
        return (bool): the return boolean of the given logic with its input
    """
    available_logicgates = ["and", "or", "nand", "nor"]
    if logic not in available_logicgates:
        raise ValueError("logic not available in logic gates list")
    if isinstance(X, bool):
        raise ValueError("X is not boolean")
    if isinstance(Y, bool):
        raise ValueError("Y is not boolean")

    def logic_and(x,y):
        if x:
            return y
        return x

    def logic_or(x,y):
        if x:
            return x
        return y

    match logic:
        case "and":
            return logic_and(X,Y)
        case "or":
            return logic_or(X,Y)
        case "nand":
            return not logic_and(X,Y)
        case "nor":
            return not logic_or(X,Y)
        case _:
            raise ValueError("internal error, check logic string from code")

def giveTrue()-> bool:
    """
        give true when the function is called

    Args:
        no parameters are expected
    Returns:
        return (bool): return true
    """
    return True

def inverse_True(data):
    """
        inverse True (inverse given boolean) when the usual convention is the opposite

    Args:
        data (Any): any given valuable type
    Returns:
        return (bool): return inverse of the conventional boolean
    """
    if data:
        return False
    return True
    