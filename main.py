from Key import Key
import random
import comfunc
import time
import rsa # external lib 


print("Input key length")
x = int(input())

start_time = time.time()

key = Key()
key.GenerateKeys(x//2)
(e, n) = key.GetPublicKey()
(d, n, q, p) = key.GetPrivateKey()
print("time passed: ------", time.time() - start_time)


print('Your Public Key is ', e , n, sep =' ')
print('Input message to encrypt')
m = input()




num = comfunc.text_to_num(m)
randc = 4;
num = comfunc.add_rand_bits(num, randc)

start_time = time.time()
c = pow(num, e,n)
print("encryption time: ------", time.time() - start_time)

start_time = time.time()
d = pow(c, d, n)
print("dencryption time: ------", time.time() - start_time)
print('Encrypted message:')
print(c)

d = comfunc.remove_rand_bits(d, 4)

s = comfunc.num_to_text(d)


print('Decrypted message')
print(s)





