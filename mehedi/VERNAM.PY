import random


def generate_key(length):
    key = ""
    for i in range(length):
        key += chr(random.randint(65, 90))  # ASCII codes for A-Z
    return key


def encrypt(plaintext, key):
    ciphertext = ""
    cipherCode = []
    for i in range(len(plaintext)):
        x = ord(plaintext[i]) ^ ord(key[i])
        cipherCode.append(x)
        ciphertext += chr(x % 26 + 65)
    return ciphertext, cipherCode


def decrypt(cipherCode, key):
    plaintext = ""
    for i in range(len(cipherCode)):
        x = (cipherCode[i] ^ ord(key[i]))
        plaintext += chr(x)
    return plaintext


plaintext = str(input('Enter plain text: '))
key = generate_key(len(plaintext))  # Generate a random key

ciphertext, cipherCode = encrypt(plaintext, key)
print("Ciphertext:", ciphertext)
decryptedtext = decrypt(cipherCode, key)
print("Decrypted text:", decryptedtext)