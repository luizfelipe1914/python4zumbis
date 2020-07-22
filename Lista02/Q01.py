#!/usr/bin/env python3
#-*- encoding:UTF-8 -*-

def main():
    a = float(input("A: "))
    b = float(input("B: "))
    c = float(input("C: "))
    if((a + b > c) or (a + c > b) or (b + c > a)):
        if((a - b < c) or (a - c < b) or (b - c < a)):
            if(a == b and a == c):
                print("Triângulo equilatero.")
            if((a == b and a != c) or (b == c and b != a)):
                print("Triângulo isósceles.")
            else:
                print("Triângulo escaleno.")
        else:
            print("Não é um triângulo!")
    else:
        print("Não é um triângulo!")

if __name__ == '__main__':
    main()
