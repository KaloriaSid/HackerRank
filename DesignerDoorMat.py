n, m = map(int, input().split())

# upper part
for i in range(n//2):
    print(('.|.' * (i * 2 + 1)).center(m, '-'))
    '''print('-' * ((m - 3)//2 - i*3), end='')
    print('.|.' * (i * 2 + 1), end='')
    print('-' * ((m - 3)//2 - i*3))'''

# middle line
print('WELCOME'.center(m, '-'))
'''print('-' * ((m - 7)//2), end='')
print('WELCOME', end='')
print('-' * ((m - 7)//2))'''

# lower part
j = n//2 - 1
for i in range(j, -1, -1):
    print(('.|.' * (i * 2 + 1)).center(m, '-'))
    '''print('-' * ((m - 3) // 2 - i * 3), end='')
    print('.|.' * (i * 2 + 1), end='')
    print('-' * ((m - 3) // 2 - i * 3))'''


'''NOTE: jo bhi code 'quotes' mei hai vo as a simple
 solution bina kisi inbuilt function ke'''
