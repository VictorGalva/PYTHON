aluno = {}

aluno['nome'] = input('Nome do aluno: ').strip()
aluno['media'] = float(input('Média do aluno: '))
if aluno['media'] < 4:
    aluno['situação'] = 'Reprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Aprovado'

print('-='*20)
for k, v in aluno.items():
    print(f'  - {k} igual a {v}')