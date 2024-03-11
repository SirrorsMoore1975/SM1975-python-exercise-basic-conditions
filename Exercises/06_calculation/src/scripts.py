"""
@param sign {"add" | "subtract" | "multiply" | "divide" | "getRemainder"} : input the sign that the calculation should perform
@param x {list} a list of numerical calculation to be performed
@param value {int} a number value that is going to apply to the list element
@returns {list} return the list that has applied the given input parameters calculation
"""




def calculation(sign: str, x: list, value: int) -> list | str :
    allowed = ["add", "subtract", "multiply", "divide", "getRemainder"]
    if sign not in allowed:
        return "sign type used is undefined"
    elif type(x) != list:
        return "x is not a list"
    elif not isinstance(value, (int, float, complex)):
        raise ValueError("{0} is not numeric".format(value))
   
    
    match sign:
        case "add":
            result = [y + value for y in x]
        case "subtract":
            result = [y - value for y in x]
        case "multiply":
            result = [y * value for y in x]
        case "divide":
            result = []
            for y in range(len(x)):
                if x[y] == 0 or value == 0:
                    result.append(0)
                else:
                    result.append(x[y] / value)
        case "getRemainder":
            result = [y % value for y in x]
    return result