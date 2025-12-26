def rail_fence_encrypt(message, rails):
    message = message.replace(" ", "").upper()
    fence = ["" for _ in range(rails)]
    rail = 0
    direction = 1

    for char in message:
        fence[rail] += char
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1

    return "".join(fence)


def rail_fence_decrypt(ciphertext, rails):
    ciphertext = ciphertext.replace(" ", "").upper()
    n = len(ciphertext)

    fence = [["" for _ in range(n)] for _ in range(rails)]

    rail = 0
    direction = 1
    for i in range(n):
        fence[rail][i] = "*"
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1

    index = 0
    for r in range(rails):
        for c in range(n):
            if fence[r][c] == "*" and index < n:
                fence[r][c] = ciphertext[index]
                index += 1

    result = []
    rail = 0
    direction = 1
    for i in range(n):
        result.append(fence[rail][i])
        rail += direction
        if rail == 0 or rail == rails - 1:
            direction *= -1

    return "".join(result)


if __name__ == "__main__":
    message = input("Enter message to encrypt: ")
    rails = int(input("Enter number of rails: "))

    encrypted = rail_fence_encrypt(message, rails)
    print("Encrypted:", encrypted)

    decrypted = rail_fence_decrypt(encrypted, rails)
    print("Decrypted:", decrypted)
