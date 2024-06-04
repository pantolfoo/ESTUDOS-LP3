# anter de usar a funcao, precisa importa-la
# importando tudo do módulo matematica para o modo main

import matematica

print(matematica.PI)
print(matematica.somar(10.0, 3.0))


# no uso: nao precisa declarar o nome do modulo
from matematica import *
print (somar(8.0, 9.0))


# USAR ASSIM
# importar só o que precisa

# de (modulo) importar (funções, constantes)
from matematica import subtrair, PI as PI_MAT

print (PI_MAT)
print (subtrair(9.0, 4.0))

from estatistica.descritiva import media, maximo, minimo