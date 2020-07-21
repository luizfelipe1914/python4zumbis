#!/usr/bin/env python3
#-*- encoding: UTF-8 -*-

def main():
    time = int(input("A quanto tempo você fuma? "))
    cigarros = int(input("Quantidade de cigarros fumada por dia: "))
    total_fumado = (cigarros * 365) * time
    lost_time = total_fumado / 144
    print("Pare de fumar! Você já perdeu %d dias de vida." %lost_time)

if __name__ == "__main__":
    main()