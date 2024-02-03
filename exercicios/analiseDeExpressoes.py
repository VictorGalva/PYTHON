# Esse cìdigo não faz nada mirabolante. Ele apenas conta se a sequência e o número
# de aberturas e fechamentos de parenteses está correto. A lógica dele é interessante.

expressao = input('Digiite uma expressão qualquer:').strip()
pilha = []
for item in expressao:
    if item == '(':
        pilha.append(item)
    elif item == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(item)
            break

print('Sua expressao é VÁLIDA!' if len(pilha) == 0 else 'Sua expressao é INVÁLIDA!')