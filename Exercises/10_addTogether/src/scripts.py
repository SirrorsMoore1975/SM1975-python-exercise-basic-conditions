def addTogether(*arrs: list[int]) -> list[int]:
    def calculate(arr1: list[int], arr2: list[int]) -> list[int]:
        m:list[int] = arr1
        n:list[int] = arr2
        result: list[int] = []
        diff: int = len(m) - len(n) # arr1 - arr2 
        if diff >= 0 :
            step:int = len(m)
            n += diff * [0]
        elif diff < 0: 
            step:int = len(n)
            m += ((-1)* diff) * [0]
        for i in range(step):
            x:list[int] = m[i]
            y:list[int] = n[i]
            result.append(x+y)
        return result
    acc:list[int] = [0]
    for j in range(len(arrs)):
        acc = calculate(acc , arrs[j])
    return acc  