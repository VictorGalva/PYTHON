# Esse programa simula progrssão aritmética ou geométrica por escolha do usuário
print('{:=^40}'.format(' Simulador de PA e PG '))

escolha = input('''\n[PA] para progressão aritimética
[PG] para progessão geométrica
Qual progressão deseja simular? ''').strip().upper()

primeiro = int(input('\nPrimeiro termo: '))
razao = int(input('Razão da progressão: '))
quantidadeTermos = int(input('Quantidade de termos que deseja ver: '))
termos = primeiro
somaDosTermos = 0

if escolha == 'PA':
    for i in range(0, quantidadeTermos): 
        print(termos, end = ' ')
        print('->' if i < quantidadeTermos - 1 else '', end = ' ')
        somaDosTermos += termos
        termos += razao
    print(f'\nA soma dos termos da PA é {somaDosTermos}')
        
elif escolha == 'PG':
    for i in range(0, quantidadeTermos):
        print(termos, end = ' ')
        print('->' if i < quantidadeTermos - 1 else '', end = ' ')
        somaDosTermos += termos
        termos *= razao 
    print(f'\nA soma dos termos da PG é {somaDosTermos}')
