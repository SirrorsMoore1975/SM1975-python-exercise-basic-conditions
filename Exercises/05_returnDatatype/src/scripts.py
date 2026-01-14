"""
@param {variable} ??? the data variable to be used in the test
@returns {string} {"number" | "boolean"| "dictionary" | "float" | "list" | "dictionary" | "tuple" | "range" | "None Type" |  "complex"  } return the name of the input parameter's datatype 
"""

def returnDatatype(input) -> str:
    datatype = {
        str : "string",
        int : "number",
        bool : "boolean",
        dict : "dictionary",
        type(None): "None Type"
    }
    data_type = type(input)
    if data_type in datatype:
        return datatype[data_type]
    return data_type.__name__
