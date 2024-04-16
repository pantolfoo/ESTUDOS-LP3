#for, while, break, continue

#operador in

for letra in "python":
    print(letra)

#exibe letra por letra


intens = ["banana", "maca", "arroz"]


for item in intens:
   print(item)

   

#>>> range(5)
#range(0, 5)
#>>> list(range(5))
#[0, 1, 2, 3, 4]
#>>> 
#range, se vc da um valor, percorre do 0 ao valor

#>>> list(range(10))
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#>>> list(range(3,10))
#[3, 4, 5, 6, 7, 8, 9]
#>>> 


for i in range(5):
    print(i)

for i in range(0,11,2):
    print (i)#0,2,4,6,8,10

lista = list(range(101))

#type devolve valor 
#>>> type(list(range(10)))
#<class 'list'>
#>>> 


#len("fghkj") devolve quantos caracteres
#len([1,2,3,4]) devolve quantos itens

#while


contador = 0
while contador <=5:
    print(contador)
    contador += 1


#break- parar totalmente

#encontre o primeiro numero par

numeros = [1,2,3,4,5,6,7]

for numero in numeros:
    if numero % 2 == 0:
        print (numero)
        break

#mostra apenas se o PRIMEIRO numero for par


#continue

numeros = [3, -1, 3, 0, -2]
for numero in numeros:
    if numero <=0:
        continue
    print (numero)


#mudando a logica
for numero in numeros:
    if numero > 0:
        continue
    print (numero)

#compreensão de lista 
#forma consisa de criar listas em python

numeros = [2, 3, 4, 5, 6]
quadrados = []

for numero in numeros:
    quadrados.append(numero ** 2)

#mapeando uma lista em outra

quadrados = [numero ** 2 for numero in numeros]

palavra = "ola mundo"
letras = [letra for letra in palavra]

#>>> pares = [numero for numero in numeros if numero %2 ==0] 
#>>> pares
#[2, 4, 6, 8]
#>>> 
