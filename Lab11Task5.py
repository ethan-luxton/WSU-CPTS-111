# Ethan Luxton
# Programming Assignment #7
# 11/25/17
# CptS 111
# Encryption Using the Logistic Map Function

def log_map(a, x):
    '''Amplitude = a, population of current gen = x'''
    return (a * x) * (1 -x)

def compare(a, n, xa, xb):
    print('Gen #', '\t\txa', '\t\t\txb', '\t\t\txa - xb')
    for i in range(1, n + 1):
        xa = log_map(a, xa)
        xb = log_map(a, xb)
        col_3 = xa - xb
        print(i, '\t\t', (xa * 96), '\t\t', (xb * 96), '\t\t', col_3)

def main():
    a = float(input("Enter the amplitude a: "))
    n = int(input("Enter the number of generations n: "))
    xa = float(input("Enter the initial population xa: "))
    xb = float(input("Enter the initial population xb: "))
    compare(a, n, xa, xb)

main()
