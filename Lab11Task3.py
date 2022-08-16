# Ethan Luxton
# Cpts 111, Lab 11
# Task 3 & 4
# November 16th, 2017
# The Caesar Cipher for Encryption: Step 2



key = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-+='

def e_d():
    global enc_dec
    enc_dec = str(input("Enter e if you want to encrypt or d if you want to decrypt: "))
    return 

def clear2cipher():
    e_d()
    if enc_dec == 'e':
        from Lab11Task1 import cipher_chr
    elif enc_dec == 'd':
        from Lab11Task1 import decipher_chr
    return

clear2cipher()

