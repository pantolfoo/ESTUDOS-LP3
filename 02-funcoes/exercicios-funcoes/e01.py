'''
Ex01 - Jogo de Adivinhação: 
Peça ao usuário para adivinhar um número entre 1 e 100 que o programa escolheu aleatoriamente. 
Informe ao usuário se o palpite está alto ou baixo, até que ele acerte o número.
'''

# biblioteca para gerar números aleatórios
import random


def adivinhar():
    numero_aleatorio = random.randint(1,100)

    while True:
        numero = int(input("Digite um número: "))
        
        if numero == numero_aleatorio:
            print('Boa, você acertou o número aleatório!')
            print()
            break
        elif numero > numero_aleatorio:
            print('Você digitou um número alto!')
            print()
                
        else:
            print('Você digitou um número baixo!')
            print()
 
adivinhar()