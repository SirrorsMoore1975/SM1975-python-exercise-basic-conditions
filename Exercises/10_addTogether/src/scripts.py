def addTogether(*arrs:list[int]) -> list[int]:
    """
        add multiple lists of number element of same index and return a list of sums of that result

    Args:
        list* (list[int]): multiple list of integers to have the same index element sum together
    Returns:
        return (list[int]): return a list of result of sum depends on index
    """
    def check_list(arr):
        if not isinstance(arr, list):
            raise ValueError("input is not list")
    def check_is_number(num):
        if not isinstance(num, int):
            raise ValueError("input is not number")
    
    def add_two_list(arr_one:list[int], arr_two:list[int]) -> list[int]:
        """
            Handle sum elements of same index from two list
            (Solution Two)
        Args:
            arr_one (list[int]): list contain integers
            arr_two (list[int]): list contain integers
        Returns:
            return (list[int]): return sum elements of same index from two list
        """
        diff = 0
        step = 0
        if len(arr_one) >= len(arr_two):
            diff += len(arr_one) - len(arr_two)
            arr_two += [0] * (diff)
            step += len(arr_one)
        else:
            diff += len(arr_two) - len(arr_one)
            arr_one += [0] * (diff)
            step += len(arr_two)
        return [arr_one[i]+ arr_two[i] for i in range(step)]
        
    
    def calculate(arr_one:list[int], arr_two:list[int]) -> list[int]:
        """
            Handle two list of integers summing the same index together
            (Solution One)

        Args:
            arr_one (list[int]): list of integers to be added
            arr_two (list[int]): list of integers to be added
        Returns:
            return (list[int]): list of integers with arr_one & arr_two same index element add together
        """
        result = []
        step = 0
        print(arr_one,"<- arr_one")
        print(arr_two,"<- arr_two")
        
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
    
    for arr in arrs:
        check_list(arr)
        for num in arr:
            check_is_number(num)
    
    acc = [0]
    # for j in range(len(arrs)):
    #     acc = calculate(acc, arrs[j])
    for _ , sublist in enumerate(arrs): 
        #acc = calculate(acc, sublist) # Solution One
        acc = add_two_list(acc, sublist) # Solution Two
    return acc