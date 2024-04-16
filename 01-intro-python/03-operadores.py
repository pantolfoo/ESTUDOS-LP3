# Operadores aritméticos
# +, -, /, *,% (resto da divisão), ** (potência)
nota1 = 10.0
nota2 = 8.0
nota3 = 5.5

media = (nota1+nota2+nota3)/3

# 10 elavado ao quadrado (2)
numero = 10

elevado_quadrado = numero*numero
elavado_quadrado = numero**2

# Operadores lógicos
# and, or, not

print (True and True) # True
print (True and False) # False
print (False and True) # False
print (False and False) # False

print (True or True) # True
print (True or False) # True
print (False or True) # True
print (False or False) # False

verdade = True and False

# permite entrada no sistema
# usuário não bloqueado E
# usuário é um funcionário E
# hora entre 8h e 18h (horário comercial)
# ---
# caso for admin pode acessar de qualquer forma

usuario_bloquado = False
usuario_funconario = True
hora = 23
usuario_admin = False

funcionario_ativo = usuario_funconario and not usuario_bloquado
horario_comercial = hora >=8 and hora <=18 # False || 23 horas

if (funcionario_ativo and horario_comercial) or usuario_admin:
    print('Acesso liberado')
else:
    print ('Acesso negado')

# Outro arquivo || usando função
# def dentro_horario_comercial(hora): # def= função 
#    return hora >=8 and hora <=18


# Operadores de comparação 
# ==, !=, >, <, >=, <=
nota1 = 10.0
nota2 = 5.5

# aluno foi melhor na prova1
if nota1>nota2:
    print('Aluno foi melhor na prova 1')

# aluno foi melhor na prova2
else:
    print('Aluno foi melhor na prova 2 ou teve a mesma nota nas duas')


# Operador is, is not
# operador de identidade
# comparar se os objetivos são os mesmos
# mesmo espaço de memória 

a = [1,2,3]
b = [1,2,3]
print (a == b) # comparar valores || True

print (a is b) # variaveis diferentes, não ocupam o mesmo espaço na memória || False

# c == b
# print (c is b) # True

# Operador in, not in
# verifica se elemento existe em uma sequência
# str, list, tupla

opcoes = ('sim', 'nao', 'talvez')
opcao = input('Digite uma opção')
opcao = opcao.lower().strip() # lower -> deixa tudo do usuário minuscula || strip-> remove espaços

if opcao in opcoes:
    print('ok')
else:
    print('inválido')







