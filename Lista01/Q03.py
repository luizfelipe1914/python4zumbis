#!/usr/bin/env python3
#-*- encoding: UTF-8 -*-

"""Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule
o total em segundos."""

def main():
    dias = int(input("Informe a quantidade de dias: "))
    horas = int(input("Informe a quantidade de horas: "))
    minutos = int(input("Informe a quantidade de minutos: "))
    total = (minutos * 60) + (horas * 3600) + ((dias * 24) * 3600)
    print(" %d dias + %d horas + %d minutos = %d segundos" %(dias, horas, minutos, total))

if __name__ == "__main__":
    main()