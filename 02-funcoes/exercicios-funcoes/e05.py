'''Ex05 - Verificador de Palíndromos: Solicite ao usuário que 
digite uma palavraou frase e verifique se é um palíndromo 
(ou seja, pode ser lida de frente para trás e de trás para frente da mesma forma).
'''

def palindromo(palavra):
    # tira espaços e deixa todas || letras minusculas (case sensitive)
    palavra = palavra.replace(' ', '').lower()

    # inverte a palavra para a verificação
    if palavra == palavra [::-1]:
        print ('A palavra digitada é um palíndromo')
    else:
        print('A palavra digitada não é um palíndromo')

palavra = input('Digite uma palavra ou frase para verificar se é palíndromo ou não: ')
palindromo(palavra)
