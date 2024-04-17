'''
Ex06 - Conversor de Notas Escolares: Baseado em uma pontuação fornecida pelo usuário (0 a 100), 
converta para o sistema de notas A, B, C, D, ou F, seguindo os padrões de conversão comuns.

'''
def conversao(nota):
    if nota >= 90:
        print('Nota A')
    elif nota >= 80:
        print('Nota B')
    elif nota >= 70:
        print('Nota C')
    elif nota>= 60:
        print('Nota D')
    elif nota < 60:
        print('Nota F')
    else: 
        print('Valor fora da faixa')
    
nota = int(input("Digite uma nota para a conversão de 0-100:"))
conversao(nota)