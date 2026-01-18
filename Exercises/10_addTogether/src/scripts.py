def addTogether(*arrs:list[int]) -> list[int]:
    """
        add multiple lists of numbers and return a list of sums of that result

    Args:
        list* (list[int]): multiple list of input to be sum together
    Returns:
        return (list[int]): return a list of result of sum depends on position 
    """
    def check_list(arr):
        if isinstance(arr, list):
            raise ValueError("input is not list")
    def check_is_number(num):
        if isinstance(num, int):
            raise ValueError("not number")
    def calculate(arr_one:list[int], arr_two:list[int]) -> list[int]:
        result = []
        diff = len(arr_one) - len(arr_two)
        if diff >= 0:
            step = len(arr_one)
            arr_two += diff * [0]
        else:
            step = len(arr_two)
            arr_one += (-1 * diff) * [0]
        for i in range(step):
            result.append(arr_one[i] + arr_two[i])
        return result
    
    # for arr in arrs:
    #     check_list(arr)
    #     for num in arr:
    #         check_is_number(num)
    
    acc = [0]
    for j in range(len(arrs)):
        acc = calculate(acc, j)
    return acc