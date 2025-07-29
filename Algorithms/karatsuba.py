import math
"""
Basic implementation of karatsubas algorithm
Time complexity = O(2^log2(3))
"""
def karatsuba(x, y):
    if x < 10 and y < 10:
        return x*y
    else:
        k = math.floor(math.log10(x)+1)
        xl = x % (math.pow(10, k//2))
        yl = y % (math.pow(10, k//2))
        xm = (x - xl) // math.pow(10, k//2)
        ym = (y - yl) // math.pow(10, k//2) 
        a = karatsuba(xm, ym)
        b = karatsuba(xl, yl)
        c = karatsuba(xm + xl, yl + ym) - a - b
        return a * math.pow(10, k) + c * math.pow(10, k//2) + b


x = 1531
y = 3453
res = karatsuba(x,y)
assert res == x * y
print(res)
