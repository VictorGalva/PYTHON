# Programa que calcula o IMC do usuário

print('{:-^40}\n'.format(' CALCULO IMC '))

peso = float(input('Qual seu peso? (kg) '))
altura = float(input('Qual sua altura? (m) '))
imc = peso / (altura ** 2)

print('Seu imc é: \033[1;37m{:.1f}\033[m'.format(imc))

if imc < 18.5:
    print('Você está \033[1;31mABAIXO DO PESO!\033[m normal')
elif 18.5 <= imc < 25:
    print('Você está com \033[1;32mPESO IDEAL!\033[m')
elif 25 <= imc < 30:
    print('Você está com       \033[1;33mSOBREPESO!\033[m')
elif 30 <= imc < 40:
    print('Você  está com \033[1;31mOBESIDADE!\033[m')
elif imc >= 40:
    print('Você está com \033[1;31mOBEDIDADE MORBIDA!\033[m')
