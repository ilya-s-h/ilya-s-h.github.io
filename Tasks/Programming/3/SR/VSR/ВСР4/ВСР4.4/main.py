
def factorial(n:int) -> int:
    result = 1
    if type(n) is int:
        if n >= 0:
            if n >= 2:
                i = 2
                while i <= n:
                    result *= i
                    i += 1
        else:
            raise ValueError("n must be greater then 0")
    else:
        raise TypeError("n must be int")
    
    return result
