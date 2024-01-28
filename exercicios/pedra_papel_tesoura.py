import random

print('='*40)
print('{: ^40}'.format(' PEDRA, PAPEL, TESOURA'))
print('='*40)
print('Jogador VS Computador')
print('OBS: O melhor de 3 vence!\n')
opcao = ['pedra', 'papel', 'tesoura']

vitoriasComput = 0
vitoriasJogador= 0
rodadas = 3
while rodadas > 0 :
    computador = random.randint(0,2)
    while True:
        try:
            jogador = int(input('''Opções
[0] pedra
[1] papel
[2] tesoura
jogador: '''))
        except ValueError:
            print('Verifique se digitou corretamente!')
            continue
        if jogador in range(0, 3):
            break
        else:
            print('Verifique se digitou corretamente!')
    print('~'*40)
    print(f'''Computador escolheu: {opcao[computador].upper()}
Jogador escolheu: {opcao[jogador].upper()}''')
    
    if computador == 0:
        if jogador == 0:
            print('EMPATE!')
        elif jogador == 1:
            print('JOGADOR VENCEU A RODADA!')
            vitoriasJogador += 1
        elif jogador == 2:
            print('COMPUTADOR VENCEU A RODADA!')
            vitoriasComput += 1
    elif computador == 1:
        if jogador == 0:
            print('COMPUTADOR VENCEU A RODADA!')
            vitoriasComput += 1
        elif jogador == 1:
            print('EMPATE!')
        elif jogador == 2:
            print('JOGADOR VENCEU A RODADA!')
            vitoriasJogador += 1
    elif computador == 2:
        if jogador == 0:
            print('JOGADOR VENCEU A RODADA!')
            vitoriasJogador += 1
        elif jogador == 1:
            print('COMPUTADOR VENCEU A RODADA!')
            vitoriasComput += 1
        elif jogador == 2:
            print('EMPATE!')
    print('~'*40)

    rodadas -= 1
print(f'''Jogador venceu {vitoriasJogador} rodadas
computador venceu {vitoriasComput} rodadas
''')
if vitoriasJogador > vitoriasComput:
    print('Jogador venceu o jogo! Até a proxima pessoal...')
elif vitoriasComput > vitoriasJogador:
    print('Computador venceu o jogo! Mais sorte na prxima...')
else:
    print('Jogo empatado! Um oponente a sua altura.')

