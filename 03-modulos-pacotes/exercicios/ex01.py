from ex01_modulo import calc_volume, pot_termostato, filtragem_hora 

def main():
    comprimento = float (input("Digite o comprimento: "))
    altura = float (input("Digite a altura: "))
    largura = float (input("Digite a largura: "))
    temp_desejada = float (input("Digite a temperatura desejada: "))
    temp_ambiente = float (input("Digite a temperatura ambiente: "))

    volume = calc_volume (comprimento, altura, largura)
    print ('O volume do aquário é:', volume)

    potencia = pot_termostato (volume, temp_ambiente, temp_desejada)
    print ('A potência do termostato necessária é: ', potencia)

    filtragem = filtragem_hora (volume)
    print ('A filtragem necessária por hora é: ', filtragem)

if __name__ == "__main__":
    main()