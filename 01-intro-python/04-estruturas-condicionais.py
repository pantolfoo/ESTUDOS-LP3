# if
idade = 20

# if condição 
#   codigo
#   codigo
#   codigo

if idade >=18:
    print('Maior de idade')

# if/ else
if idade>= 18:
        print('Maior de idade')
else:
      print('Menor de idade')

# if/ elif/ else
# criança = 0 - 12
# adolescente = 13 - 17
# adulto = 18 - 59
# idoso = 60+

if idade <=12:
      print ('criança')
elif idade <=17:
      print ('adolescente')
elif idade <=59:
      print ('Adulto')
else:
      print('Idoso')      


# exemplo de if aninhado 
email = 'isabella@gmail.com'
senha= '123'

if email == 'isabella@gmail.com':
    if senha == '123': 
          print ('acesso permitido')
    else:
          print('invalido')
else:
      print('invalido')

# melhorado:

if(email == 'isabella@gmail.com' and senha=='123'):
      print('valido')
else:
      print('inválido')


# entrada numero
# 0 - domingo
# 1 - segunda
# 2 - terça
# 3 - quarta
# 4 - quinta
# 5 - sexta


dia =1

if dia == 1:
      print('Domingo')
elif dia == 2:
      print('Segunda')      

# usando dicionário:

dias ={
      1: 'domingo',
      2: 'segunda',
      3: 'terca',
      4: 'quarta',
      5: 'quinta',
      6: 'sexta',
      7: 'sabado'
}
if dia in dias:
      print (dias[dia])