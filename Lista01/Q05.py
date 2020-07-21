#!/usr/bin/env python3
#-*- encoding: UTF-8 -*-

def main():
    preco = float(input("Informe o preço da mercadoria: R$ "))
    desconto = float(input("Percentual de desconto: "))
    print("Preço original: R$ %.2f" %preco)
    print("Desconto: R$ %.2f" %(preco * (desconto / 100)))
    print("Preço final: R$ %.2f" %(preco - (preco * (desconto / 100))))


if __name__ == "__main__":
    main()