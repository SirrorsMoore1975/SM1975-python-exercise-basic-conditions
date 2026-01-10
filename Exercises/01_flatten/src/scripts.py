"""
Write a function called flatten that takes an array of arrays and returns a flattened version
Do not use internal build-it method

@param {list} ??? a list of lists
@returns {list} ??? a flattened list of the list of lists
"""

def flatten(my_list:list) -> list:
    """
    flatten nested list into one level list
    
    Args:
        my_list(list): list to be flatten
    
    Returns:
        result(list): flattened list
    """
    # Solution 1

    # result = []
    # for ele in my_list:
    #     if isinstance(ele, list):
    #         result += flatten(ele)
    #     else:
    #         result.append(ele)
    # return result

    # Solution 2
    def is_list(the_list):
        return isinstance(the_list, list)
    return [ele for sublist in my_list for ele in (sublist if is_list(sublist) else [sublist])]