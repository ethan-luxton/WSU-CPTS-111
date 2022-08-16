# Ethan Luxton
# Lab 11, Task 1 & 2
# November 16th, 2017
# The Caesar Cipher for Encryption: Step 1
key = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-+=:;''""\/|~'
n = int(input("Enter the rotation: "))

def cipher_chr(n):
    line = input('Enter line to cipher: ')
    """Encrypt the string and return the ciphertext"""
    result = ''
    for l in line:
        i = (key.index(l) + n) % 95
        result += key[i]
    print(result.upper())
    return

def main():
    cipher_chr(n)
    return

main()
