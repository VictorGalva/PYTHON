print('{:~^60}\n'.format(' IDENTIFICADOR DE PALINDROMOS '))
print('OBS: No caso de frases e palavras, desconsidere o uso de acentos.')
entrada = input('Digite qualquer coisa (palavra, frase, números): ').strip()

junto = ''.join(entrada.split())
contrario = junto[::-1]

print(f'{junto.upper()} ao contrario fica {contrario}, por isso', end = ' ')

if junto.lower() == contrario:
    print('se trata de um palindromo.')
else:
    print('não se trata de um palindromo.')