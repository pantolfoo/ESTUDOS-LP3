'''
Ex04 - Simulador de Eleições: Crie um programa que simule uma votação com três candidatos. 
O programa deve pedir ao usuário para votar várias vezes e, no final, 
mostrar o número de votos de cada candidato e quem foi o vencedor.
'''

candidato_1 = 0 # lala
candidato_2 = 0 # momota
candidato_3 = 0 # querido



def votacao(candidato_1, candidato_2, candidato_3):
    contador = 0
    while (contador < 3):
        print('Em quem você deseja votar?')
        voto = int(input('1 - Latorre || 2 - Motta || 3 - Quirino '))
        print()

        if(voto == 1 or voto == 2 or voto == 3):
            contador = contador + 1

            if (voto == 1):
                print ('você votou no Latorre')
                candidato_1 += 1
            elif (voto == 2):
                print ('você votou no Motta')
                candidato_2 += 1
            else:
                print ('você votou no Quirino')
                candidato_3 +=1
    print()
    print ('Votação encerrada, vamos as apurações')

def contagem(candidato_1, candidato_2, candidato_3):
    if (candidato_1 > candidato_2 and candidato_1 > candidato_3):
        print('Latorre ganhou!')
    elif (candidato_2 > candidato_1 and candidato_2 > candidato_3):
        print('Motta ganhou!')
    elif (candidato_3 > candidato_1 and candidato_3 > candidato_2):
        print('Quirino ganhou!')
    else:
        print('Ocorreu um empate, vote novamente!')
        votacao(candidato_1, candidato_2, candidato_3)
        contagem(candidato_1, candidato_2, candidato_3)

        # vai direto pro else e reinicia o programa


votacao (candidato_1, candidato_2, candidato_3)
contagem (candidato_1, candidato_2, candidato_3)