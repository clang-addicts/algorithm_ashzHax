def print_formatted(number):
    # your code goes here
    _len = len(str(bin(number)[2:]))
    for i in range(1, number+1):
        print(str(i).rjust(_len, ' '), end=' ')
        print(oct(i)[2:].rjust(_len, ' '), end=' ')
        print(hex(i)[2:].upper().rjust(_len, ' '), end=' ')
        print(bin(i)[2:].rjust(_len, ' '))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)