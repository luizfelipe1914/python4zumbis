#!/usr/bin/env python3
#-*- encoding: UTF-8 -*-

def main():
    ano = int(input("Informe o ano: "))
    if(ano % 4 == 0 and ano % 100 != 0):
        print("Bissexto!")
    elif(ano % 400 == 0):
        print("Bissexto!")
    else:
        print("Não é Bissexto!")

if __name__ == '__main__':
    main()
