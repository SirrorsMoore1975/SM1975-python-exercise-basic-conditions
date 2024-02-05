"""
Write a function called flatten that takes an array of arrays and returns a flattened version
Do not use internal build-it method

@param {list} ??? a list of lists
@returns {list} ??? a flattened list of the list of lists
"""

def flatten(_list):
    result = []
    for ele in _list:
        if isinstance(ele, list):
            result += flatten(ele)
            # for item in ele:
            #     result.append(item)
        else: 
            result.append(ele)
    return result