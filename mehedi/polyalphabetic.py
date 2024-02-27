def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string)-len(key)):
            key.append(key[i%len(key)])
    return("".join(key))
def encrypt(string, key):
    cipher = []
    for i in range(len(string)):
        x = (ord(string[i])+ord(key[i]))%26 + 65
        cipher.append(chr(x))
    return("".join(cipher))
def decrypt(cipher, key):
    plain=[]
    for i in range(len(cipher)):
        x = (ord(cipher[i])-ord(key[i]))%26 + 65
        plain.append(chr(x))
    return("".join(plain))
string = input('Enter message: ')
keyword = input('Enter key: ')
key = generateKey(string, keyword)
print('Cipher: ',encrypt(string, key))
cipher = encrypt(string,key)
print('Plain: ', decrypt(cipher, key))