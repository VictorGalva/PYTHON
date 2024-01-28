reta1 = float(input('Primeira reta:'))
reta2 = float(input('Segunda reta:'))
reta3 = float(input('Terceira reta:'))
if (reta1 + reta2) > reta3 and (reta1 + reta3) > reta2 and (reta2 + reta3) > reta1:
    print('Os três segmentos de reta formam um triângulo',end = ' ')
    if reta1 == reta2 and reta2 == reta3:
        print('equilátero (quando todos os lados tem mesma medidda).')
    elif reta1 != reta2 and reta2 != reta3 and reta3 != reta1:
        print('escaleno (quando todos os lados possuem medidas diferentes).')
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print('isósceles (quando existem dois lados com mesma medida).')
else:
    print('Os três segmentos de reta não formam um triângulo')
