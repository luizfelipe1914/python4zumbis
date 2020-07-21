#!/usr/bin/env python3
#-*- encoding: UTF-8 -*-

def main():
    velocity = float(input("Velocidade média(Km/h): "))
    space = float(input("Distância a ser percorrida(Km): "))
    time = space / velocity
    print("O tempo de viagem estimado é de %d horas." % time)

if __name__ == "__main__":
    main()