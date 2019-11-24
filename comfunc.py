import random

def is_prime( x): #using ferma 100 times
    if x == 2:
        return True
    k = min(100, x)
    while k != 0:
        a = random.randint(1, x - 1)
        if pow(a, x-1, x) != 1:
                #print(a)
            return False
        k = k - 1
    return True

def ext_gcd(a,b):
    x = 1
    y = 0
    ta = a
    tb = b
        
    x1 = 0
    y1 = 1
    while b != 1:
        (a, b) = (b, a%b)
        (x, x1) = (x1 - (a//b)*x, x)
        (y, y1) = (y1 - (a//b)*y, y)
    if x1 < 0:
        x1 = x1 + tb
    if y1 < 0:
        y1 = y1 + ta
    return (a, x1, y1)
