numeros = []
while True:
    num = int(input('Informe o número: '))
    if num in numeros:
        print('O número informado já se encontra na lista!')
    else:
        numeros.append(num)
        print('Numero adicionado com sucesso!')
    resp = input('Deseja informar mais números? [S/N]').strip()[0]
    if resp.upper() == 'S':
        continue
    elif resp.upper() == 'N':
        print('Lista encerrada.')
        break
numeros.sort()
print(f'Números adicionados a lista: {numeros}')
