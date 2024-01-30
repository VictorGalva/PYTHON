from random import choice
from os import system, name
bonequinho = [ 
    '''
    +----------+
    |          |
    |          
    |         
    |
    |
    |
....|..................
    ''',
    '''
    +----------+
    |          |
    |          O
    |         
    |
    |
    |
....|..................
    ''',
    '''
    +----------+
    |          |
    |          O 
    |         /
    |
    |
    |
....|..................
    ''',
    '''
    +----------+
    |          |
    |          O
    |         /|
    |
    |
    |
....|..................
    ''',
    '''
    +----------+
    |          |
    |          O
    |         /|\\
    |
    |
    |
....|..................
    ''',
    '''
    +----------+
    |          |
    |          O
    |         /|\\
    |         /
    |
    |
....|..................
    ''',
    '''
    +----------+
    |          |
    |          O
    |         /|\\
    |         / \\
    |
    |
....|................
        ''',
'''<<<<<<<<<< JOGO DA FORCA DO VITO >>>>>>>>>>''']

def limpaTela():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = ('clear')

class hangMen():
    def __init__(self, palavra):
        self.palavra = palavra
        self.palavraDescoberta = ['_' for x in palavra]
        self.letrasErradas = []

    def tentativaUsuario(self, letra):
        if letra in self.palavra:
            index = 0
            for item in self.palavra:
                if letra == item:
                    self.palavraDescoberta[index] = letra
                index += 1
        else:
            if letra not in self.letrasErradas:
                self.letrasErradas.append(letra)

    def fimDoJogo(self):
        if self.jogadorVenceu() or (len(self.letrasErradas) == 6):
            return True
        return False
    
    def jogadorVenceu(self):
        if '_' not in self.palavraDescoberta:
            return True
        return False
    
        
    def statusGame(self):
        print(bonequinho[-1])
        print(bonequinho[len(self.letrasErradas)])
        print('\nPalavra: {}'.format(''.join(self.palavraDescoberta)))
        print('\nLetras erradas: {}'.format(' '.join(self.letrasErradas).upper()))

def palavraDaRodada(listaDePalavras):
    palavra = choice(listaDePalavras)
    return palavra

frutas = ['melância', 'uva', 'banana', 'pitaia', 'caju']

def iniciarGame():
    
    limpaTela()

    start = hangMen(palavraDaRodada(frutas))

    while not start.fimDoJogo():
        start.statusGame()

        while True:
            try:
                entradaUsuario = input('\ninforme a letra: ')
            except entradaUsuario.isalpha() == False:
                continue
            if entradaUsuario.isalpha() and len(entradaUsuario) == 1:
                break
            else:
                print('Verifique se digitou o que foi pedido!')

        start.tentativaUsuario(entradaUsuario)

    start.statusGame()

    if start.jogadorVenceu():
        print('\nParabens! Tchau :)')

    else:
        print(f'\nQue pena! A palavra era {start.palavra}')
        print('Mais sorte na proxima :(')

if __name__ == '__main__':
    iniciarGame()
