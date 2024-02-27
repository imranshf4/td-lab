def ceaserE(plain_Text, shift):  # Plain Text and Shifting Letters to Encrypt.
    ciphertext = ''
    for letters in plain_Text:
        if letters == ' ':
            ciphertext = ciphertext + letters
        elif letters.isupper():
            ciphertext = ciphertext + chr((ord(letters) + shift - 65) % 26 + 65)
        else:
            ciphertext = ciphertext + chr((ord(letters) + shift - 97) % 26 + 97)
    return ciphertext

def ceaserD(cipher_Text, key):
    plaintext = ''
    for letters in cipher_Text:
        if letters == ' ':
            plaintext = plaintext + letters
        elif letters.isupper():
            plaintext = plaintext + chr((ord(letters) - key - 65) % 26 + 65)
        else:
            plaintext = plaintext + chr((ord(letters) - key - 97) % 26 + 97)

    return plaintext



plain_Text = input("Enter message to Encrypt: ")
shift1 = int(input("Enter key for encryption: "))
cipher_Text = ceaserE(plain_Text, shift1)
print("Encryption message: ",cipher_Text)
for i in range(1,27):
    shift = i
    print("Decription messasge: ",ceaserD(cipher_Text, shift))


