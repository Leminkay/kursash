from Key import Key
import random
import comfunc
import time
import rsa # external lib 








ferm = 0
lib = 0
rm = 0



for i in range(10000):
    a= random.randint(2**512,2**513)
    start_time = time.time()
    t1  = comfunc.ftest(a)
    ferm +=time.time() - start_time
    start_time = time.time()
    t2 = comfunc.rmtest(a)
    rm = time.time() - start_time
    if t1 != t2:
        print(a)

print(ferm/100, rm /100)


print("Input key length")
x = int(input())
 

key = Key()
start_time = time.time()
key.GenerateKeysFermat(x//2)
#(e, n) = key.GetPublicKey()
#(d, n, q, p) = key.GetPrivateKey()
#print("fermat")
#print("time passed: ------", time.time() - start_time)
ferm += time.time() - start_time
print(ferm)
#print('Your Public Key is ', e , n, sep =' ')

start_time = time.time()
#print(rm test)
key.GenerateKeysRM(x//2)
rm += time.time() - start_time
#print("rsa lib")
print(rm)


start_time = time.time()

(pub, priv) = rsa.newkeys(x)

   # print("time passed: ------", time.time() - start_time)
lib += time.time() - start_time
print(lib)


print('Input message to encrypt')
m = input()


(e, n) = key.GetPublicKey()
(d,n,q,p) = key.GetPrivateKey()
num = comfunc.text_to_num(m)
randc = 4;
num = comfunc.add_rand_bits(num, randc)

#encrypting
c = pow(num, e,n)


#decrypting
d = pow(c, d, n)

#print('Encrypted message:')
#print(c)

d = comfunc.remove_rand_bits(d, 4)

s = comfunc.num_to_text(d)


#print('Decrypted message')
#print(s)


mr = m.encode('utf8')



crypt = rsa.encrypt(mr, pub)



dec = rsa.decrypt(crypt, priv)

