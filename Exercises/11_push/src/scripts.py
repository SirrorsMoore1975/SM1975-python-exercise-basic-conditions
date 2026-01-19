def push(my_list:list, add_element) -> int:
    """
        push add_element to my_list and update my_list

    Args:
        my_list (list): list to be added with new element
        add_element (any): element to be added to the list

    Returns:
        return (int): new length of the list
    """
    my_list += [add_element]
    return len(my_list)

