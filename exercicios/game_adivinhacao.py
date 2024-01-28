from random import randint,uniform
from time import sleep

print('- ' * 20)
print('{:^40}'.format('GAME DE ADIVINHAÇÃO'))
print('- ' * 20, '\n')

computador  = randint(0,20)
print('Adivinhe o número que o computador vai sortear entre 0 e 20. Você tera 4 chances.\n')
chances = 4

while chances > 0: 
    while True:
        try:
            jogador = int(input('Informe o número: '))
        except ValueError:
            print('ERRO! Tente novamente.')
            continue
        if jogador in range (0, 21):
            break
        else:
            print('Verifique se digitou corretamente!')

    if jogador > computador:
        print('Errou! O número é menor.\n')
    elif jogador < computador:
        print('Errou! O número é maior.\n')
    else:
        print('Paranbéns. Você acertou o número!')
        break
    
    chances -= 1

if chances == 0:
    print(f'O número sorteado foi {computador}')
    print('Acabaram as chances. Mais sorte na proxima...')




