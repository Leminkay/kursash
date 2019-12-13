import random
import math
import comfunc

    
class Key(object):
    _e = 65537
    _p = 0
    _q = 0
    _d = 0
    _n = 0
                       
    
    
    def GeneratePrimeFermat(self,bitl):
        self._p = random.randint(2**(bitl - 1), 2**bitl - 1)
        self._q = random.randint(2**(bitl - 1), 2**bitl - 1)
        while comfunc.ftest(self._p) == False :
            self._p = random.randint(2**(bitl - 1), 2**bitl - 1)
        while comfunc.ftest(self._q) == False :
            self._q = random.randint(2**(bitl - 1), 2**bitl - 1)
            
    def GeneratePrimeRM(self,bitl):
        self._p = random.randint(2**(bitl - 1), 2**bitl - 1)
        self._q = random.randint(2**(bitl - 1), 2**bitl - 1)
        while comfunc.rmtest(self._p) == False :
            self._p = random.randint(2**(bitl - 1), 2**bitl - 1)
        while comfunc.rmtest(self._q) == False :
            self._q = random.randint(2**(bitl - 1), 2**bitl - 1)   

    
    def GenerateKeysFermat(self,bitl): #returns _e,d,n where ed = 1(mod phi)
        self.GeneratePrimeFermat(bitl)
        self._n = self._q * self._p
        phi = (self._q - 1)*(self._p - 1)
        
        div, self._d, t = comfunc.ext_gcd(self._e,phi)

        return self._e, self._d, self._n
    def GenerateKeysRM(self,bitl): #returns _e,d,n where ed = 1(mod phi)
        self.GeneratePrimeRM(bitl)
        self._n = self._q * self._p
        phi = (self._q - 1)*(self._p - 1)
        
        div, self._d, t = comfunc.ext_gcd(self._e,phi)

        return self._e, self._d, self._n
    def GetPublicKey(self):
        return self._e,self._n

    
    def GetPrivateKey(self):
        return self._d,self._n,self._q,self._p



