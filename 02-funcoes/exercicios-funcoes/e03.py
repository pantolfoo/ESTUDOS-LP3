'''
Ex03 - Contador de Vogais e Consoantes: 
Peça ao usuário para digitar uma frase e retorne o número de vogais e consoantes na frase.
'''
def contador(frase):
    qtd_vogais = 0
    qtd_consoantes = 0
    vogais = 'aeiouAEIOU'

    for char in frase:
        if char in vogais:
            qtd_vogais +=1

        elif char.isalpha():
            qtd_consoantes +=1

    return qtd_vogais, qtd_consoantes
    

frase = input('Digite uma frase para a contagem: ')
vogais, consoantes = contador(frase)

print()
print(f'Quantidade de vogais: {vogais}')
print(f'quantidade de consoantes: {consoantes}')
print()