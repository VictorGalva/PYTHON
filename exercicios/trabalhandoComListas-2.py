print('{:-^40}'.format(' AAAAAAAAALUNOS '))
alunos = []
while True:
    registro = []
    notas = []
    soma = 0
    registro.append(input('Nome do aluno: ').strip())
    for i in range(0, 2):
        notas.append(float(input(f'{i+1}ª nota: ')))
        soma += notas[i]
    media = soma / 2
    registro.append(notas)
    registro.append(media)
    alunos.append(registro)
    continuar = input('Deseja registrar mais alunos? [S/N] ').strip()[0]
    if continuar in 'Nn':
        break
print('-='*20)
print('{: <10}{: ^10}{: >10}'.format('INDICE', 'NOME', 'MÉDIA'))
print('-'*40)
for aluno in alunos:
    print('{: <10}{: ^10}{: >10}'.format(alunos.index(aluno), aluno[0], aluno[2]))
print('-'*40)

while True:
    entrada = input('Deseja ver as notas de um aluno em específico? [S/N]').strip()[0]
    if entrada in 'Nn':
        break
    else:
        while True:
            indiceAluno = int(input('Indice do aluno: '))
            if  (len(alunos) * (-1)) > indiceAluno  or indiceAluno > (len(alunos) - 1):
                print('Indexação incorreta!')
            else:
                break
        print('-'*40)
        print('{}{: >5}{: >5}'.format('NOME', '1ª NOTA', '2ª NOTA'))
        print('{}{: >5}{: >5}'.format(alunos[indiceAluno][0], alunos[indiceAluno][1][0], alunos[indiceAluno][1][1]))
        print('-'*40)
