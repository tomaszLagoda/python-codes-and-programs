def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    result = 1
    for x in range(1, exp+1):
        if x == 1:
            result = base
        else:
            result = result * base
    return result

def iterPowerRecursive(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp == 0:
        result = 1
    else:
        result = base * iterPowerRecursive(base, exp -1)
    return result

x = float(input("What is the base number (Int or Float): "))
y = int(input("What is the exponential number (integer): "))

result = iterPower(x,y)
print( "Iterative result:", result)


result = iterPowerRecursive(x,y)
print( "Recursive result:", result)