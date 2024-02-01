# O código a seguir pede 3 seguimentos de reta ao usuário
# e informa se eles podem formar um triângulo e qual o tipo de triângulo
# eles foramam.
class triangulo:
    def __init__(self, lado1=1, lado2=1, lado3=1):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def tipoTriangulo(self):
        if (self.lado1 + self.lado2) > self.lado3 and (self.lado1 + self.lado3) > self.lado2 and (self.lado2 + self.lado3) > self.lado1:
            print('Os três segmentos de reta formam um triangulo do tipo', end=' ')
            if self.lado1 == self.lado2 and self.lado2 == self.lado3:
                print('equilátero (quando todos os lados tem mesma medidda).')
            elif self.lado1 != self.lado2 and self.lado2 != self.lado3 and self.lado3 != self.lado1:
                print('escaleno (quando todos os lados possuem medidas diferentes).')
            elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
                print('isósceles (quando existem dois lados com mesma medida).')
        else:
            print('Os três segmentos de reta não formam um triângulo!')



reta1 = float(input('Informe a primeira reta: '))
reta2 = float(input('Informe a segunda reta: '))
reta3 = float(input('Informe a terceira reta: '))

trianguloTeste = triangulo(reta1, reta2, reta3)
trianguloTeste.tipoTriangulo()

