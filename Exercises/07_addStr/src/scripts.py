def addStr(args:tuple):
    
    try:
        result = ""
        for i in args:
            if type(i) == 'int':
                result += str(i)
            else:
                result += i
        return result
    except TypeError:
        return "TypeError: args not tuple"
    
    
    # for l in args:
    #     if type(l) == 'int':
    #         l = str(l)
    #     result += l
    