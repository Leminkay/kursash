from rss import Key
import random


print("Input key length")
x = int(input())

key = Key()
key.GenerateKeys(x//2)
(e, n) = key.GetPublicKey()
(d, n) = key.GetPrivateKey()
print('Your Public Key is ', e , n, sep =' ')
print('Input message to encrypt')
m = input()

num = 0;
for i in m:
    num <<= 8
    num += ord(i)
num<<=4
num += random.randint(2**4,2**5 - 1)
c = pow(num, e,n)
d = pow(c, d, n)
print('Encrypted message:')
print(c)

s = ''
d >>= 4
d -= 1
while d != 0:
    s += str(chr((d % ( 2**8))))
    d = d//(2**8)
s = s[len(s)::-1]
print('Decrypted message')
print(s)





