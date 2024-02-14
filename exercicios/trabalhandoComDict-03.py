from datetime import date
pessoa = {}
pessoa['Nome'] = input('Nome da pessoa: ').strip()
nasc = int(input('Ano de nascimento: '))
pessoa['Idade'] = date.today().year - nasc
pessoa['CTPS'] = int(input('Carteira de trabalho (digite 0 se não tiver): '))
if pessoa['CTPS'] != 0:
    pessoa['Ano de contratação'] = int(input('Em que ano foi contratado(a): '))
    pessoa['salário'] = float(input('Infome seu salário: R$'))
    pessoa['Idade de aposentadoria'] = (pessoa['Ano de contratação'] - nasc) + 35

print('-='*20)
for k, v in pessoa.items():
    if k == 'salário':
        print(f'  - {k} igual a R${v:.2f}')
        continue
    print(f'  - {k} igual a {v}')