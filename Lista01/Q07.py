#!/usr/bin/env python3
#-*- encoding: UTF-8 -*-

def main():
    c = float(input("Informe a temperatura em  Celsius: "))
    f = ((9 * c)/5) + 32
    print("Fahrenheit: %.2f" %f)

if __name__ == "__main__":
    main()