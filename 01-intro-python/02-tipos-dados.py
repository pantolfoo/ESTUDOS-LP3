# Tipos


# 1. Numericos (int, float,complex)
# Int:
idade = 10
temperatatura = -20

# Float: 
altura = 165.4

# 2. Bool
verdadeiro = True
mentira = False


# 3. String (sequencia de caracteres)
nome = 'Isa'
nome = "Isinha"

# Multilinha 
frase = ''' Oier,
Como você está?
Teste
123 
'''

# Interpolacao de string
nome = "Isabella Pantolfo"
idade = 17
frase = f"Olá {nome}. Você tem {idade} anos!" #{} irá aparecer os dados que estao definidos a cima
print(frase)

# Char (string de um caractere)
letra = 'a'
letra = "a"

# Acesso de um caractere da String 
nome = "Simone Dambrosio"
print (nome[0]) # primeira posicao do nome Simone 'S'
print (nome[-1]) # leitura de tras pra frente 'o'
print (nome[-3]) # leitura de tras pra frente 's'

# String sao objetos, logo sao metodos
print(nome.capitalize()) # Simone dambrosio
print(nome.upper()) # SIMONE DAMBROSIO


# 4. list (listas)
# indexada, pode ser alterada
habilidades = []
habilidades = ['python', 'html', 'java'] # lista:com colchetes

# acessar um item da lista
habilidades[1] # 'html'

# adicionar um item no final da lista
habilidades.append('C#') # python, html, java, C#

# inserir em posicao especifica 
habilidades.insert(2, 'css') # 2: posicao// python, css, html, java, C#
print(habilidades)

# limpar
#habilidades.clear()
#print(habilidades) #[]

# For
for habilidade in habilidades: # p cada habilidade DENTRO da lista habilidades...
    print(habilidade) # exibe habilidades

def somar (n1, n2):
    return n1+n2
somar(10.0, 20.0)


# 5. tuple (tupla)
# 'lista' de valores
# listas imutáveis, uma vez criadas, não podem ser alteradas, nem adicionar itens.
opcoes = ('sim', 'nao', 'talvez') # tupla: com parenteses

print(opcoes[0])
for opcao in opcoes:
    print(opcao)

# set (conjunto)
# conjunto de valores
# nao permite elementos duplicados, nao é indexado

habilidades = {'python', 'java', 'C#', 'java'}
print(habilidades) #{'java', 'python', 'C#'}


# 6. dict (dicionario)
# palavra -> definico
# chave -> valor
# key -> value
# conjunto de chave valor

nome = "Bruno Pantolfo"
idade= 18 
habilidades = ['mecatronica', 'eletronica', 'eletrotecnica']
empregado = True

#objeto:
canditato = {
    'nome': 'Bruno Pantolfo', #chave valor
    'idade': 18,
    'habilidades': ['mecatronica', 'eletronica', 'eletrotecnica'], 
    'empregado': True
}

print(canditato['nome']) # nome do canditado // Bruno Pantolfo
print(canditato.keys()) # somente as chaves // (['nome', 'idade', 'habilidades', 'empregado'])
print(canditato.values()) # somente valores // (['Bruno Pantolfo', 18, ['mecatronica', 'eletronica', 'eletrotecnica'], True])


# 7. None 
nome = None 