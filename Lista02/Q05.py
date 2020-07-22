#!/usr/bin/env python3
#-*- encoding: UTF-8 -*-

def main():
    numbers = []
    for i in range(0, 3, 1):
        numbers.append(int(input("%dº número: " %(i+1))))
    i = 0
    maior = numbers[0]
    menor = maior
    while(i < 3):
        if(numbers[i] > maior):
            maior = numbers[i]
        else:
            if(numbers[i] < menor):
                menor = numbers[i]
        i = i + 1
    print("O menor é %d e o maior é %d" %(menor, maior))

if __name__ == '__main__':
    main()
