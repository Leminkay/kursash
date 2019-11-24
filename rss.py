import random
import math
import comfunc

    
class Key(object):
    _e = 65537
    _p = 0
    _q = 0
    _d = 0
    _n = 0
            
    '''
    def ext_gcd(a, b): # returns (g,x,y) for a*x+b*y= g
        if a == 0:
            return (b, 0, 1)
        g, x, y = ext_gcd(b % a, a)
        
        return (g, y - (b//a)*x, x)
    '''
            
    
    
    def GeneratePrime(self,bitl):
        self._p = random.randint(2**(bitl - 1), 2**bitl - 1)
        self._q = random.randint(2**(bitl - 1), 2**bitl - 1)
        while comfunc.is_prime(self._p) == False :
            self._p = random.randint(2**(bitl - 1), 2**bitl - 1)
        while comfunc.is_prime(self._q) == False :
            self._q = random.randint(2**(bitl - 1), 2**bitl - 1)
        

    
    def GenerateKeys(self,bitl): #returns _e,d,n where ed = 1(mod phi)
        self.GeneratePrime(bitl)
        self._n = self._q * self._p
        phi = (self._q - 1)*(self._p - 1)
        
        div, self._d, t = comfunc.ext_gcd(self._e,phi)

        return self._e, self._d, self._n
    
    def GetPublicKey(self):
        return self._e,self._n

    
    def GetPrivateKey(self):
        return self._d,self._n


if __name__ == '__main__':
    key = Key()
    ##print(key.GeneratePrime(256))
   
    print(key.GenerateKeys(10))
    print(key._q)
    print(key._p)
    print(key.GetPublicKey())
    print(key.GetPrivateKey())
