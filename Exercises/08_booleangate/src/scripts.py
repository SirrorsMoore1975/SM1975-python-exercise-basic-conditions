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

def booleangate_not(A):
    return not A

def booleangate(logic, x, y):
    match logic:
        case "and":
            if x:
                return y
            else:
                return x
        case "or":
            if y:
                return x
            else:
                return y
        case _:
            return "logic not defined"
    pass

def giveTrue():
    return True

def inverse_True(data):
    if (data) :
        return True
    else:
        return False
    