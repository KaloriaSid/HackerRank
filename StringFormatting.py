def print_formatted(number):
    l = len(bin(number).replace('0b', ''))
    for i in range(1, n+1):
        print(str(i).rjust(l), end=' ')
        print(oct(i).replace('0o', '').rjust(l), end=' ')
        print(hex(i).replace('0x', '').upper().rjust(l), end=' ')
        print(bin(i).replace('0b', '').rjust(l))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
