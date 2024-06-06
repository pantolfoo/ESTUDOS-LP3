def calc_volume(comprimento, altura, largura):
    volume = (comprimento * altura *  largura) / 1000
    return volume

def pot_termostato (volume, temp_desejada, temp_ambiente):
    potencia = volume * 0.05 * (temp_desejada - temp_ambiente)
    return potencia

def filtragem_hora(volume):
    filtragem = volume *2
    return filtragem

