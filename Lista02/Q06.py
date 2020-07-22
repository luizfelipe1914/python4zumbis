#!/usr/bin/env python3
#-*- encoding: UTF-8 -*-

def main():
    salario = float(input("Salário-hora: R$ "))
    tempo = int(input("Quantidade de horas trabalhadas: "))
    ir = (salario * tempo) * (11/100)
    inss = (salario * tempo)* (8/100)
    sindicato = (salario * tempo) * (5/100)
    print("+ Salário bruto: R$", (salario * tempo) )
    print("- IR (11%): R$",  ir)
    print("- INSS(8%): R$", inss)
    print("- Sindicato(5%): R$",  sindicato)
    print("Salário Líquido : R$ ", ((salario * tempo) - (ir + inss + sindicato)))

if __name__ == '__main__':
    main()
