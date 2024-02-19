jogadores = []
jogador = {}
gols = []
while True:
    jogador.clear()
    gols.clear()
    jogador['Nome'] = input('Nome do jogador: ').strip()
    numPartidas = int(input(f'Numero de partidas que {jogador["Nome"]} jogou: '))
    for i in range(0, numPartidas):
        numGols = int(input(f'   Número de na {i+1}ª paritda: '))
        gols.append(numGols)
    jogador['Gols por partida'] = gols[:]
    totalGols = sum(jogador['Gols por partida'])
    jogador['Total'] = totalGols
    jogadores.append(jogador.copy())
    while True:
        cont = input('Deseja continuar? [S/N] ').strip().upper()[0]
        if cont in 'SN':
            break
        else:
            print('Digite corretamente!')
    if cont == 'N':
        break

print('-='*28)
print(f'{"INDICE": <10}{"NOME": <16}{"GOLS": ^20}{"TOTAL": >10}')
print('-'*56)
for p in jogadores:
    print('{: <10}{: <16}{: ^20}{: >10}'.format(jogadores.index(p), p["Nome"], str(p["Gols por partida"]), p["Total"]))
print('-='*28)
while True:
    while True:
        cont = input('Analisar um jogador individualmente? [S/N]').strip().upper()[0]
        if cont in 'SN':
            break
        else:
            print('Digite corretamente!')
    if cont == 'N':
        break
    print('-='*28)
    while True:
        index = int(input('Informe o indice do jogador: '))
        if index < 0 or index > len(jogadores) - 1:
            print('Indice inválido!')
        else:
            break
    jogador = jogadores[index]
    print(f'O jogador {jogador["Nome"]} fez {jogador["Total"]} gols em {len(jogador["Gols por partida"])} partidas.')
    for c in range(0, len(jogador['Gols por partida'])):
        print(f'  => Fez {jogador["Gols por partida"][c]} gols na {c+1}ª partida.' if jogador['Gols por partida'][c] > 1 else f'  => Fez {jogador["Gols por partida"][c]} gol na {c+1}ª partida.')

    print('-='*28)

print('<< FIM >>')
