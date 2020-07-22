#!/usr/bin/env python3
#-*- encoding: UTF-8 -*-

def main():
    area = float(input("Área: "))
    volume = area / 3
    qtd_latas = volume // 18
    teste = volume % 18
    if(teste != 0):
        qtd_latas += 1
    print("Área:  M²", area)
    print("Total de Litros:", volume)
    print("Quantidade de latas de tinta: ", qtd_latas)
    print("Total: R$ %s0" %(str(qtd_latas * 80.00).replace(".", ",")))

if __name__ == '__main__':
    main()
