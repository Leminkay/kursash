from Key import Key
import random
import comfunc
import time
import rsa # external lib 

def speed_test():
    f_timer = 0
    l_timer = 0
    rm_timer = 0

    t = 100

    for i in range(t):
        keyf = Key()
        keyrm = Key()
        
        bitl = 512
        m = "tempmesmesmes"
        #testinf fermat
        start_time = time.time()
        keyf.GenerateKeysFermat(bitl//2)
        (e, n) = keyf.GetPublicKey()
        (d,n,q,p) = keyf.GetPrivateKey()
        num = comfunc.text_to_num(m)
        c = pow(num, e,n)
        d = pow(c, d, n)
        f_timer += time.time() - start_time
        #test rm
        start_time = time.time()
        keyrm.GenerateKeysRM(bitl//2)
        (e, n) = keyrm.GetPublicKey()
        (d,n,q,p) = keyrm.GetPrivateKey()
        num = comfunc.text_to_num(m)
        c = pow(num, e,n)
        d = pow(c, d, n)
        rm_timer += time.time() - start_time
        #test lib
        start_time = time.time()
        (pub, priv) = rsa.newkeys(bitl)
        ms = m.encode("utf8")
        c = rsa.encrypt(ms, pub)
        d = rsa.decrypt(c, priv)
        ms = ms.decode("utf8")
        l_timer += time.time() - start_time

    print("512 bit len crypt encrypt time:")
    print("for fermat test: ", f_timer / t)
    print("for frm test: ", rm_timer / t)
    print("for rsa lib test: ", l_timer / t) 

speed_test()
