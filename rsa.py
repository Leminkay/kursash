from rss import Key
from sys import getdefaultencoding
x = int(input())

key = Key()
key.GenerateKeys(x)
(e, n) = key.GetPublicKey()
(d, n) = key.GetPrivateKey()

m = int(input())
c = pow(m, e, n)
d = pow(c, d, n)
print(c)
print(d)



