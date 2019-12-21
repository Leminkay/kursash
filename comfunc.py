import random

def ftest(x): #using fermat 100 times
    if x == 2:
        return True
    k = min(100, x)
    while k != 0:
        a = random.randint(1, x - 1)
        if pow(a, x-1, x) != 1:
                #print(a)
            return False
        k -= 1
    return True

def rmtest(x): # rabin-miller test
    if x == 2:
        return True
    if x % 2 == 0 or x < 2:
        return False
    
    n = x - 1
    s = 0
    while n % 2 == 0:
        n >>= 1
        s += 1
    
    k = 10
    
    for i in range(k):
        
        a = random.randint(2, x - 2)
        t = pow(a, n, x)
        
        if t == 1 or t == x - 1:
            continue

        
        flag = 0
        
        for j in range(s - 1):
            t = pow(t, 2 ,x)

            if t == 1:
                return False
            
            if t == x - 1:
                flag = 1
                break
        if flag == 0:
            return False
        
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

def gcd(a, b):
    return gcd(b, a % b) if b != 0 else a


def next_prime_rm(x):
    if x % 2 == 0:
        x += 1
    while rmtest(x) == False:
        x += 2
    return x
def next_prime_f(x):
    if x % 2 == 0:
        x += 1
    while ftest(x) == False:
        x += 2
    return x

def text_to_num(s):
    num = 0;
    for i in s:
        num <<= 8
        num += ord(i)
    return num

def add_rand_bits(num, cnt):
    num<<=cnt
    num += random.randint(2**cnt,2**(cnt + 1) - 1)
    return num

def remove_rand_bits(num, cnt):
    num >>= cnt
    num -= 1
    return num

def num_to_text(num):
    s = ''
    while num != 0:
        s += str(chr((num % ( 2**8))))
        num = num//(2**8)
    s = s[len(s)::-1]
    return s

