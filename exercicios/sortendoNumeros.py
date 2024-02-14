from random import randint

print('{:=^40}\n'.format(' criador de apostas '))
numApostas = int(input('Quantas apostas deseja criar? '))
print('\n','-='*20)
for i in range(0, numApostas):
    palpite = []
    while len(palpite) < 6:
        num = randint(1, 61)
        if num not in palpite:
            palpite.append(num)
        palpite.sort()
    print(f'Jogo {i+1}: {palpite}')
print('-='*20)