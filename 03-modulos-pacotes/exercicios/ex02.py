'''
Ex02. Utilizando as diretrizes de Índice de Massa Corporal (IMC) da Organização Mundial de Saúde (OMS),
crie uma calculadora que solicita ao usuário seu peso (Kg) e sua altura (m) e apresenta em qual classificação o indivíduo se encaixa. 
Além disso, o programa deve apresentar quanto o indivíduo precisa perder ou ganhar de peso para chegar no peso normal (imc = 24,9).

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

from ex02_modulo import calcular_imc, classificacao_imc, diferenca_peso


def main():
    peso_entrada = float (input("Digite o seu peso (Kg): "))
    altura = float (input("Digite a altura(m): "))

    imc = calcular_imc(peso_entrada, altura)
    classificacao = classificacao_imc(imc, altura)

    print('Seu imc é: ', imc)
    print('Sua classificação é: ', classificacao)


    if imc != 24.9:
        diferenca = diferenca_peso(imc, altura)
        if imc > 24.9:
            print(f"Você precisa perder {diferenca:.2f} kg para atingir o peso normal.")
        else:
            print(f"Você precisa ganhar {abs(diferenca):.2f} kg para atingir o peso normal.")



if __name__ == "__main__":
    main()
    