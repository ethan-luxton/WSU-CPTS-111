key = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-+='
n = int(input("Enter the rotation: "))

def decipher_chr(n):
    ciphertext = str(input("Enter your ciphertext: "))
    """Decrypt the string and return the plaintext"""
    result = ''

    for l in ciphertext:
        i = (key.index(l) - n) % 75
        result += key[i]

    print(result.upper())

    return

def main():
    decipher_chr(n)
    return

main()