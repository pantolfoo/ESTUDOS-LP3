# Identificadores
# letras, numeros e 
# case sensitive (maiusculo ou minusculo faz diferença)
# palavras reservadas(palavras que nao podem ser usadas para nomes de variaveis): if, for, class, main
idade = 20
Idade = 20

# Variaveis 
# Java: float velocidade=20.2f; //velocidade = identificador, float = tipo
nome = "Maria da Silva"
velocidade = 20.2
velocidade = velocidade + 10.0

# Constante
# Java: final float velocidade=20.2f;
# Python: nao tem constante
# convencao: identifica uma constante com as letras maiusculas 
PI = 3.14

# Comenatrio de uma linha 

'''
comentario
de 
multiplas 
linhas
'''

# docstring 
# documentar codigo de funcoes, calsses, etc

def somar(numero1, numero2): 
    # validar se os tipos sao numericos (p realizar a soma)
    '''
    funcao que soma dois numeros

    :param //parametro// numero1: primeiro numero
    :param //parametro// numero2: segundo numero
    :return: soma dos numeros
    '''
    return numero1+numero2

somar(10,0,2.0)
