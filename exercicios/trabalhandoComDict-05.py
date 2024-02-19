pessoas = []
pessoa = {}
soma = 0
while True: 
    pessoa['Nome'] = input('Informe o nome: ').strip()
    while True:
        pessoa['Sexo'] = input('Informe o sexo [M/F]: ').strip().upper()
        if pessoa['Sexo'] in 'MF':
            break
        else:
            print('Digite novamente!')
    pessoa['Idade'] = int(input('Informe a idade: '))
    soma += pessoa['Idade']
    pessoas.append(pessoa.copy())
    while True:
        continuar = input('Deseja informar mais pessoas? [S/N] ').strip().upper()
        if continuar in 'SN':
            break
        else:
            print('Digite corretamente!')
    if continuar == 'N':
        break
media = soma / len(pessoas)
print('-='*30)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
print(f'B) A média de idade das pessoas é de {media:.2f} anos.')
print(f'C) As mulheres cadastradas foram', end=' ')
for item in pessoas:
    if item['Sexo'] == 'F':
        print(item['Nome'], end=', ')
print()
print('D) Listas das pessoas acima da média de idade: ')
for i in range(0, len(pessoas)):
    if pessoas[i]['Idade'] > media:
        for k, v in pessoas[i].items():
            print(f'  {k} = {v:}', end='; ')
        print()
        

    