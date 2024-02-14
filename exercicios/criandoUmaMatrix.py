matriz = [[], [], []]

for l in  range(0, 3):
    for c in range(0, 3):
        matriz[l].append(int(input(f'Informe um valor para a linha {l} e coluna {c}: ')))
print('-='*30)
somaPares = 0
somaColuna3 = 0
for linha in matriz:
    for coluna in linha:
        if coluna % 2 == 0:
            somaPares += coluna
        if linha.index(coluna) == 2:
            somaColuna3 += coluna
        print(f'[{coluna:^5}]', end=' ')
    print()
print('-='*30)
print(f'Soma dos valores pares da matriz: {somaPares}')
print(f'Soma dos valores da terceira coluna: {somaColuna3}')
print(f'O maior valor da segunda linha é: {max(matriz[1])}')
