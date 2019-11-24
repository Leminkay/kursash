from rss import Key
x = int(input())

key = Key()
key.GenerateKeys(x)
print(key.GetPublicKey())
print(key.GetPrivateKey())

