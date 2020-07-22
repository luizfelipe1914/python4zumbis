#!/usr/bin/env python3
#-*- encoding: UTF-8 -*-

def main():
    number_1 = int(input("1º Número: "))
    number_2 = int(input("2º Número: "))
    number_3 = int(input("3º Número: "))
    if(number_1 > number_2 and number_1 > number_3):
        print("O maior é:  %d" %number_1)
    elif(number_2 > number_1 and number_2 > number_3):
        print("O maior é: %d" %number_2)
    elif(number_3 > number_1 and number_3 > number_2):
        print("O maior é: %d" %number_3)
    else:
        print("Os valores informados são iguais.")

if __name__ == '__main__':
    main()
