"""
@param {variable} ??? the data variable to be used in the test
@returns {string} {"number" | "boolean"| "dictionary" | "float" | "list" | "dictionary" | "tuple" | "range" | "None Type" |  "complex"  } return the name of the input parameter's datatype 
"""

def returnDatatype(x) ->str:
    
    specialName = {
        int: "number",
        str: "string",
        bool: "boolean",
        dict: "dictionary",
        type(None): "None Type"
    }

    data_type = type(x)
    if data_type in specialName:
        return specialName[data_type]
    else:
        return data_type.__name__
