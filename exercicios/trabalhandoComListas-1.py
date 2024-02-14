numeros = [[], []]

for i in range(0, 7):
    num = int(input(f'Digite o {i+1}º valor: '))
    if num % 2 == 0: 
        numeros[0].append(num)
    else:
        numeros[1].append(num)

print(f'Valores pares da lista: {sorted(numeros[0])}')
print(f'Valores ímpares da lista: {sorted(numeros[1])}')