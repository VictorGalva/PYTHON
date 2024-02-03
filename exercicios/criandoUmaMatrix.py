matriz = [[], [], []]

for l in  range(0, 3):
    for c in range(0, 3):
        matriz[l].append(int(input(f'Informe um valor para a linha {l} e coluna {c}: ')))
print('-='*30)
for linha in matriz:
    for coluna in linha:
        print(f'[{coluna:^5}]', end=' ')
    print()
