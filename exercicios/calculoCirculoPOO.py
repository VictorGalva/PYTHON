# O programa a seguir pede ao usuário que informe o raio de um circulo 
# e exibe a area e o perimetro utiilizando POO.
class circulo:

    pi = 3.14

    def __init__(self, raio=1):
        self.raio = raio

    def printArea(self):
        area = circulo.pi * self.raio ** 2
        print(f'A area do circulo é igual a {area}')

    def printPerimetro(self):
        perimetro = 2 * circulo.pi * self.raio
        print(f'O perimetro do circulo é igual a {perimetro}')

raio = float(input('Informe o raio do circulo: '))
circulo1 = circulo(raio)

# Mostrar a area do circulo 
circulo1.printArea()
# Mostrar o perimetro do circulo
circulo1.printPerimetro()
print(circulo1.raio)