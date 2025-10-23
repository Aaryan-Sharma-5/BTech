def removeSpaces(plain):
    n = len(plain)
    temp = ""
    for i in range(n):
        if plain[i] != ' ':
            temp += plain[i]
    return temp

def toLowerCase(string):
    return string.lower()

def generateKeyTable(keyT):
    keyT.clear()
    for i in range(5):
        keyT.append([0]*5)
    alphabet = "abcdefghiklmnopqrstuvwxyz"  
    
    row = 0
    col = 0
    for char in alphabet:
        keyT[row][col] = char
        col += 1
        if col == 5:
            row += 1
            col = 0

def search(keyT, a, b, arr):
    if a == 'j':
        a = 'i'
    if b == 'j':
        b = 'i'

    for i in range(5):
        for j in range(5):
            if keyT[i][j] == a:
                arr[0] = i
                arr[1] = j
            elif keyT[i][j] == b:
                arr[2] = i
                arr[3] = j

def prepare(string):
    result = ""
    i = 0
    while i < len(string):
        result += string[i]
        if i + 1 < len(string) and string[i] == string[i + 1]:
            result += 'x' 
        i += 1
    
    if len(result) % 2 != 0:
        result += 'x'
    return result

def encrypt(string, keyT):
    n = len(string)
    arr = [0]*4

    result = list(string)
    for i in range(0, n, 2):
        search(keyT, result[i], result[i+1], arr)

        if arr[0] == arr[2]:
            result[i] = keyT[arr[0]][(arr[1] + 1) % 5]
            result[i+1] = keyT[arr[0]][(arr[3] + 1) % 5]
        elif arr[1] == arr[3]:
            result[i] = keyT[(arr[0] + 1) % 5][arr[1]]
            result[i+1] = keyT[(arr[2] + 1) % 5][arr[1]]
        else:
            result[i] = keyT[arr[0]][arr[3]]
            result[i+1] = keyT[arr[2]][arr[1]]

    return ''.join(result)

def encryptByPlayfairCipher(string):
    keyT = []
    string = toLowerCase(removeSpaces(string))
    string = prepare(string)
    generateKeyTable(keyT)
    return encrypt(string, keyT)

def decrypt(string, keyT):
    n = len(string)
    arr = [0]*4

    result = list(string)
    for i in range(0, n, 2):
        search(keyT, result[i], result[i+1], arr)

        if arr[0] == arr[2]:
            result[i] = keyT[arr[0]][(arr[1] - 1) % 5]
            result[i+1] = keyT[arr[0]][(arr[3] - 1) % 5]
        elif arr[1] == arr[3]:
            result[i] = keyT[(arr[0] - 1) % 5][arr[1]]
            result[i+1] = keyT[(arr[2] - 1) % 5][arr[1]]
        else:
            result[i] = keyT[arr[0]][arr[3]]
            result[i+1] = keyT[arr[2]][arr[1]]

    return ''.join(result)

def decryptByPlayfairCipher(string):
    keyT = []
    string = toLowerCase(removeSpaces(string))
    generateKeyTable(keyT)
    return decrypt(string, keyT)

def printKeyTable(keyT):
    print("Key Table:")
    for i in range(5):
        for j in range(5):
            print(keyT[i][j], end=" ")
        print()
    print()

keyT = []
generateKeyTable(keyT)
printKeyTable(keyT)

string = input("Enter the string to encrypt: ")
string = toLowerCase(removeSpaces(string))
string = prepare(string)

encrypted_text = encryptByPlayfairCipher(string)
print("Cipher text:", encrypted_text)

decrypted_text = decryptByPlayfairCipher(encrypted_text)
print("Decrypted text:", decrypted_text)
print()
