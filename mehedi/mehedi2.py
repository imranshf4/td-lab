def encrypt(text, s):
    result = " "

    for i in range(len(text)):
        char = text[i]

        #uppercase char encrypt
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        else:
            result += chr((ord(char) + s-97) % 26 + 97)
    return result


text = str(input('Enter plain text: '))
shifting = int(input("Enter shifting value: "))

print("Text : " + text)
print("Shift : " + str(shifting))
print("Cipher text: " + encrypt(text, shifting))
