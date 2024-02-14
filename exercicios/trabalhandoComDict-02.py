from random import randint
from time import sleep
from operator import itemgetter
jogadores = {}

for i in range(1, 5):
    jogadores[f'jogador-0{i}'] = randint(1, 6)

for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.5)

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

print('-='*20)
print('  == RANKING JOGADORES == ')
for c in range(0, len(ranking)):
    print(f'    {c+1}º lugar: {ranking[c][0]}')