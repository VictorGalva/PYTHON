# O programa a seguir armazena numeros informados pelo usuário em uma lista
# e organiza ao mesmo tempo em ordem crescente.
numeros = []

for i in range(0, 5):
    num = int(input('Informe o número: '))
    if i == 0 or num > numeros[-1]:
        numeros.append(num)
        print('Numero adicionado ao final da lista.')
    else:
        index = 0
        while index < len(numeros):
            if num <= numeros[index]:
                numeros.insert(index, num)
                print(f'Numero adicionado na posição {index} da lista.')
                break
            index += 1

print(f'A lista, organizada automaticamente, ficou assim: {numeros}.')
