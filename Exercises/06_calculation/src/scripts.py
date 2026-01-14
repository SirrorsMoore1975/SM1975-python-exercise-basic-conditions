"""
@param sign {"add" | "subtract" | "multiply" | "divide" | "getRemainder"} : input the sign that the calculation should perform
@param x {list} a list of numerical calculation to be performed
@param value {int} a number value that is going to apply to the list element
@returns {list} return the list that has applied the given input parameters calculation
"""




def calculation(sign: str, data_list: list, value: int | float| complex):
    """
    iterate a number with a list of number with the given mathematical sign 

    Args:
        sign(str): mathematic sign as string
        data_list(list): list of numerical number 
    Returns:

    """
    def check_params():

        allowed = ["add", "subtract", "multiply", "divide", "getRemainder"]
        if sign not in allowed:
            raise ValueError("sign type used is undefined") 
        if not isinstance(data_list, list):
            raise ValueError("data_list is not a list") 
        if not all(isinstance(x, (int, float, complex)) for x in data_list):
            raise ValueError("data_list element has non number") 
        if not isinstance(value, (int, float, complex)):
            raise ValueError(f"{value} is not numeric")
    check_params()
    x = data_list
    match sign:
        case "add":
            result = [y + value for y in x]
        case "subtract":
            result = [y - value for y in x]
        case "multiply":
            result = [y * value for y in x]
        case "divide":
            result = []
            for y,_ in enumerate(x):
                if x[y] == 0 or value == 0:
                    result.append(0)
                else:
                    result.append(x[y] / value)
        case "getRemainder":
            result = [y % value for y in x]
    return result
