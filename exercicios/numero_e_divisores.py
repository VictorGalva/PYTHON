# O seguinte programa recebe um número do usuário e informa se ele é primo ou não.
# Os divisores do número apareceram de amarelo.

num = int(input('Digite um número: '))
divisores = 0
for c in range(1, num+1):
    if num % c == 0:
        divisores += 1
        print('\033[4;33m{}\033[m'.format(c),end = ' ')
    else:
        print('\033[4;36m{}\033[m'.format(c),end = ' ')
if divisores > 2:
    print('\nO número {} possuí {} divisores, portanto não é primo'.format(num, divisores,))
else:
    print('\nO número {} possui {} divisores, portanto é primo'.format(num, divisores))