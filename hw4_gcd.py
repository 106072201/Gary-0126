#-*- coding: utf-8 -*-


def compute_gcd(a,b):
    # your code here ...
    while a >=b :
        a=a%b
        if a == 0:
            return b
        b=b%a
        if b == 0:
            return a
    while a < b:
        b=b%a
        if b == 0:
            return a
        a=a%b
        if a == 0:
            return b

a = int(input("輸入第一個數字: "))
b = int(input("輸入第二個數字; "))
print(a, '和', b, '的最大公因數是', compute_gcd(a,b))             