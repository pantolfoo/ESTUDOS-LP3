'''
Ex02 - Tabuada de Um Número: 
Solicite ao usuário um número e exiba a tabuada desse número de 1 a 10.
'''

def tabuada(entrada):
    print()
    contador = 0
    while(contador<=10):
        resultado = entrada * contador
        print( f'{entrada} x {contador} = {resultado}')
        contador=contador+1
 
entrada = int(input("Digite um número para ver a tabuada de 1 a 10: "))
tabuada(entrada)
