def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    test = a
    result = 1

    if b > a:
        test = b
    
    while test > 1:
        if a % test == 0 and b % test == 0:
            result = test
            break
        test -= 1

    return result

def gcdIterRecursive(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        return a
    return gcdIterRecursive(b, a % b)


x = int(input("Provide x: "))
y = int(input("Provide y: "))

result = gcdIter(x,y)
print( "Using iterative approach: The greatest common divisor of " + str(x) + " and " + str(y) + " is ", result)


result = gcdIterRecursive(x,y)
print( "Using recursive approach: The greatest common divisor of " + str(x) + " and " + str(y) + " is ", result)