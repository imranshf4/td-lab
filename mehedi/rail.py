def main():
    plaintext = input("Enter plaintext: ")
    key = input("Enter key: ")

    rem = len(plaintext) % len(key)
    barti_letter = ''.join(chr(ord('a') + (26 - rem + i + 1)) for i in range(rem - 1))

    plaintext += barti_letter

    mp = {}  # dictionary to store characters column-wise
    print("Key is:", key, "\nPlaintext:\n", plaintext, "\nMatrix is:\n")

    # matrix display key-wise
    for i in range(0, len(plaintext), len(key)):
        for j in range(len(key)):
            if (key[j] not in mp):
                mp[key[j]] = []
            mp[key[j]].append(plaintext[i + j])
            print(plaintext[i + j], end=" ")
        print()

    print()

    # final output for rail fence cipher technique
    encryp = ""
    for k, v in mp.items():
        encryp += ''.join(v)

    print("Encryption is:", encryp)

    # Decryption part
    demp = {}
    k = 1  # for map index
    for i in range(0, len(encryp), len(key)):
        demp[k] = list(encryp[i:i + len(key)])
        k += 1

    print("\nDecryption matrix----\n")
    for j in key:
        for i in range(len(demp[int(j)])):
            print(demp[int(j)][i], end=" ")
        print()

    decryp = ""
    print("\nDecryption Reverse matrix is:")
    for k in range(len(encryp) // len(key)):
        for j in key:
            print(demp[int(j)][k], end=" ")
            decryp += demp[int(j)][k]
        print()

    print("\nDecryption text is:\n", decryp)


if __name__ == "__main__":
    main()
