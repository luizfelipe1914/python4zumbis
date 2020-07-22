#!/usr/bin/env python3
#-*- encoding: UTF-8 -*-

def main():
    peso = float(input("Peso total: "))
    if(peso > 50.00):
        excesso = peso - 50.00
        multa = excesso * 4.00
    else:
        excesso = multa = 0.00
    print("Total pescado: %s00 Kg" %str(peso).replace(".",","))
    print("Excesso: %s00 Kg" %str(peso).replace(".",","))
    print("Multa: R$ %s0" %str(multa).replace(".", ","))

if __name__ == "__main__":
    main()
