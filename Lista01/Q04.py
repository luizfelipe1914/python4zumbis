#!/usr/bin/env python3
#-*- encoding: UTF-8 -*-


def main():
    salario = float(input("Informe o valor do salário: R$ "))
    aumento = float(input("Informe o percentual de aumento: "))
    novo_salario = salario + (salario * (aumento / 100))
    print("O novo salario é R$ %.2f " %novo_salario)

if __name__ == "__main__":
    main()