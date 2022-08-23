# Ethan Luxton
# Programming Assignment #7
# 11/25/17
# CptS 111
# Encryption Using the Logistic Map Function

from gen_amp_seed import *
from Lab11Task5 import *
from Lab11Task1 import *
def cipher_encrypt():
    password = input('Enter password: ')
    amp, seed = gen_amp_seed(password)
    line = input('Enter line to cipher: ')
    
