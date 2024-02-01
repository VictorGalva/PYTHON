numeros = []
for n in range(0, 5):
    num = int(input(f'Informe o número para a posição {n}: '))
    numeros.append(num)
    if n == 0:
        maior = menor = numeros[n]
    else:
        if numeros[n] > maior:
            maior = numeros[n]
        if numeros[n] < menor:
            menor = numeros[n]

print('-='*30)
print(f'Lista dos valores digitados: {numeros}')
print(f'O maior valor digitado foi {maior}, nas posições' if numeros.count(maior) > 1 else f'O maior valor digitado foi {maior}, na posição', end=' ')
for index, item in enumerate(numeros):
    if item == maior:
        print(index, end='... ')

print(f'\nO menor valor digitado foi {menor}, nas posições' if numeros.count(menor) > 1 else f'\nO menor valor digitado foi {menor}, na posição', end=' ')
for index, item in enumerate(numeros):
    if item == menor:
        print(index, end='... ')
