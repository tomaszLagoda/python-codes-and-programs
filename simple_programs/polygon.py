import math

def polysum(n, s):
    area =  (0.25 * n * s**2) / math.tan( math.pi / n )
    perimeter = n * s

    return round(area + (perimeter**2), 4)

n = int(input("Provide n: "))
s = int(input("Provide s: "))

result = polysum(n,s)
print( "Sum of polygon area and permiter square is ", result)