jogador = {}
jogador['Nome'] = input('Nome do jogador: ').strip()
numPartidas = int(input('Quantas partidas ele jogou? '))
gols = []
for i in range(0, numPartidas):
    num = int(input(f'  Quantos gols o jogador fez na {i+1}ª partida? '))
    gols.append(num)
jogador['Gols por partida'] = gols
jogador['Total'] = sum(jogador['Gols por partida'])
print('-='*20)
print(jogador)
print('-='*20)
for k, v in jogador.items():
    print(f'{k}: {v}')
print('-='*20)
print(f'O jogador {jogador["Nome"]} jogou {numPartidas} partidas.')
for i, v in enumerate(jogador['Gols por partida']):
    print(f'  => Na {i+1}ª partida ele marcou {v} gol' if v == 1 else f'  => Na {i+1}ª partida ele marcou {v} gols.')
 