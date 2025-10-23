def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    def egcd(a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = egcd(b % a, a)
            return (g, x - (b // a) * y, y)

    g, x, y = egcd(e, phi)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % phi

def generate_keys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 17 
    if gcd(e, phi) != 1:
        raise Exception("e and phi(n) are not coprime!")

    d = mod_inverse(e, phi)
    return (n, e, d)

def encryption(message, e, n):
    return pow(message, e, n)

def decryption(ciphertext, d, n):
    return pow(ciphertext, d, n)

p = 61
q = 53
message = 23

n, e, d = generate_keys(p, q)
ciphertext = encryption(message, e, n)
decrypted = decryption(ciphertext, d, n)

print(f'Public Key (n, e): ({n}, {e})')
print(f'Private Key (n, d): ({n}, {d})')
print(f'Original Message: {message}')
print(f'Ciphertext: {ciphertext}')
print(f'Decrypted Message: {decrypted}')
