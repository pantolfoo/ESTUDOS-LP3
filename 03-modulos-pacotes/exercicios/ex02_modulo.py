'''
IMC = peso / altura * altura

Classificação
----------------------------------
IMC           Classificação
-----------------------------------
< 18,5             Baixo peso
18,5 a 24,9     Peso normal
25,0 a 29,9     Excesso de peso
30,0 a 34,9     Obesidade de Classe 1
35,0 a 39,9     Obesidade de Classe 2
>= 40,00         Obesidade de Classe 3

'''



def calcular_imc(peso_entrada, altura):
    return peso_entrada / (altura ** 2)


def classificacao_imc(imc):
    if imc < 18.5:
        return 'peso baixo'
    
    elif 18.5 <= imc <= 24.9:
        return 'Peso normal'
    
    elif 25.0 <= imc <= 29.9:
        return 'Excesso de peso'

    elif 30.0 <= imc <= 34.9:
        return 'Obesidade de Classe 1'

    elif 35.0 <= imc <= 39.9:
        return 'Obesidade de Classe 2'
    
    else: 
        return 'Obesidade de Classe 3'
    

def diferenca_peso(imc_atual, altura):
    peso_normal = 24.9 * (altura ** 2)
    peso_necessario = peso_normal - imc_atual * (altura ** 2)
    return peso_necessario