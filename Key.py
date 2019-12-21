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
        rand = random.randint(2**(bitl - 1), 2**bitl - 1)
        self._p = comfunc.next_prime_f(rand)
        
        self._q = self._p
        while self._q == self._p :
            rand = random.randint(2**(bitl - 1), 2**bitl - 1)
            self._q = comfunc.next_prime_f(rand)


        
    def GeneratePrimeRM(self,bitl):

        rand = random.randint(2**(bitl - 1), 2**bitl - 1)
        self._p = comfunc.next_prime_rm(rand)
        
        self._q = self._p
        while self._q == self._p :
            rand = random.randint(2**(bitl - 1), 2**bitl - 1)
            self._q = comfunc.next_prime_rm(rand)

    
    def GenerateKeysFermat(self,bitl): #returns _e,d,n where ed = 1(mod phi)
        phi = self._e
        while comfunc.gcd(phi, self._e) != 1:
            self.GeneratePrimeFermat(bitl)
            self._n = self._q * self._p
            phi = (self._q - 1)*(self._p - 1)
        
        div, self._d, t = comfunc.ext_gcd(self._e,phi)

        return self._e, self._d, self._n
    
    def GenerateKeysRM(self,bitl): #returns _e,d,n where ed = 1(mod phi)
        phi = self._e
        while comfunc.gcd(phi, self._e) != 1:
            self.GeneratePrimeRM(bitl)
            self._n = self._q * self._p
            phi = (self._q - 1)*(self._p - 1)

        div, self._d, t = comfunc.ext_gcd(self._e,phi)
            
        return self._e, self._d, self._n
    
    def GetPublicKey(self):
        return self._e,self._n

    
    def GetPrivateKey(self):
        return self._d,self._n,self._q,self._p



