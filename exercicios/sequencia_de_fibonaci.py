# O seguinte programa mostra quantos números o usuário desejar da sequência de Fibonaci

print('-=-'*10)
print('{: ^30}'.format('Sequencia de Fibonaci'))
print('-=-'*10,'\n')
qtde = int(input('Quantos números da sequência você deseja ver? '))
termo1 = 0
termo2 = 1
print('{}→'.format(termo1), end = ' ')
print('{}→'.format(termo2), end = ' ')
i = 0
while i < (qtde - 2):
	prox = termo1 + termo2
	print('{} →'.format(prox), end = ' ')
	termo1 = termo2 
	termo2 = prox
	i += 1
print('FIM')
