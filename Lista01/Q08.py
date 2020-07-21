#!/usr/bin/env python3
#-*- encoding: UTF-8 -*-

def main():
    f = float(input("F° : "))
    c = (((f-32)*5) / 9)
    print("C° = %.2f" % c)

if __name__ == "__main__":
    main()