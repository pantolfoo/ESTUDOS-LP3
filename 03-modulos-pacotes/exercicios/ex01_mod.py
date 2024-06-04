'''
    Volume é dado por (comprimento * altura * largura) / 1000
    A potência do termostato depende do tamanho do aquário 
    e da temperatura ambiente. 
    Para o cálculo utilizar a fórmula: 
    potencia = volume * 0,05 * (temperatura desejada - temperatura ambiente)
    A quantidade de filtragem por hora deve ser no mínimo 2 a 3 vezes o volume do aquário.
'''

from ex01 import comprimento, altura, largura, temp_desejada, temp_ambiente


def volume(comprimento, altura, largura):
    return (comprimento * altura *  largura) / 1000

def pot_termostato (volume, temp_desejada, temp_ambiente):
    return volume * 0.05 * (temp_desejada - temp_ambiente)