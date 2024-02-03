pessoas = []
registro = []
maisLeve = maisPesado = 0
while True:
    registro.append(input('Informe o nome: ').strip())
    registro.append(float(input('Informe o peso: ')))
    if len(pessoas) == 0:
        maisLeve = maisPesado = registro[1]
    else:
        if maisPesado < registro[1]:
            maisPesado = registro[1]
        if maisLeve > registro[1]:
            maisLeve = registro[1]
    pessoas.append(registro[:])
    registro.clear()
    continuar = input('Deseja continuar? [S/N] ').strip()[0]
    if continuar in 'Nn':
        break
print('-*'*40)
print(f'Ao todo foram cadastradas {len(pessoas)} pessoas')
print(f'Menor peso registrado: {maisLeve}kg. As pessoas mais leves são: ', end=' ')
for item in pessoas:
    if item[1] == maisLeve:
        print(item[0], end=' ')
print(f'\nMaior peso registrado: {maisPesado}kg. As pessoas mais pesadas são:', end=' ')
for item in pessoas:
    if item[1] == maisPesado:
        print(item[0], end=' ')
