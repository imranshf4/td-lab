global cipher 
global cipher_text
def create_matrix(key):
    key = key.upper()
    matrix = [[0 for i in range(5)] for j in range(5)]
    letters_added = []
    row = 0
    col = 0
    for letter in key:
        if letter not in letters_added:
            matrix[row][col] = letter
            letters_added.append(letter)
        else:
            continue
        if col == 4:
            col = 0
            row = row + 1
        else:
            col = col + 1
    for letter in range(65,91):
        if letter == 74:
            continue
        if chr(letter) not in letters_added:
            letters_added.append(chr(letter))
    index = 0
    for i in range(5):
        for j in range(5):
            matrix[i][j] = letters_added[index]
            index = index + 1
    return matrix

def separate_same_letters(message):
    index = 0
    while(index<len(message)):
        letter1 = message[index]
        if index == len(message) -1:
            message = message + 'X'
            index = index + 2
            continue
        letter2 = message[index + 1]
        if letter1 == letter2:
            message  = message[:index + 1] + "X" + message[index + 1:]
        index = index + 2
    return message

def indexOf(letter,matrix):
    for i in range(5):
        try:
            index = matrix[i].index(letter)
            return (i, index)
        except:
            continue
def playfair(key, message, encrypt = True):
    inc = 1
    if encrypt == False:
        inc = -1
    matrix = create_matrix(key)
    message = message.upper()
    message = message.replace(' ','')
    message = separate_same_letters(message)
    cipher_text = ''
    cipher = ''
    for(letter1, letter2) in zip(message[0::2], message[1::2]):
        row1,col1 = indexOf(letter1, matrix)
        row2,col2 = indexOf(letter2, matrix)
        if row1 == row2:
            cipher_text += matrix[row1][(col1 + inc)%5] + matrix[row2][(col2 + inc)%5]
            cipher = cipher_text
        elif col1 == col2:
            cipher_text += matrix[(row1+inc)%5][col1] + matrix[(row2 + inc)%5][col2]
            cipher = cipher_text
        else:
            cipher_text += matrix[row1][col2] + matrix[row2][col1]
            cipher = cipher_text


    return cipher_text

message = input('Enter plain text: ')
key = input('Enter key: ')
print('Encrypting: ')
print(playfair(key,message))
encrypt_message = playfair(key, message)
print('Decrypting: ')
print(playfair(key,encrypt_message, False))
    
