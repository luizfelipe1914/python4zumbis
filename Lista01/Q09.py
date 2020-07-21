#!/usr/bin/env python3
#-*- encoding: UTF-8 -*-

def main():
    km = float(input("Quantidade de km rodados: "))
    dias = int(input("Quantidade de dias: "))
    total = dias * 60 + km * 0.15
    print("O preco total é: R$ %s0" % str(total).replace(".", ","))

if __name__ == "__main__":
    main()