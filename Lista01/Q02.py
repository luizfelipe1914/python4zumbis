#!/usr/bin/env python3
#-*- encoding: UTF-8 -*-

# 2) Escreva um programa que leia um valor em metros e o exiba convertido em milímetros.

def main():
    medida = int(input("Informe a medida em metros: "))
    print("A medida é %dmm" %(medida * 1000))


if __name__ == "__main__":
    main()