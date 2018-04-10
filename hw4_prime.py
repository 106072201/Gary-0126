#-*- coding:utf-8 -*-


def is_prime(num):
    # your code here ...
    if num ==2:
        return True
    for i in range(2, int(num**(1/2)_+1)):
        if num % i ==0:
            return False
    return True


num = int(input("Enter a number:"))

if is_prime(num):
    print(num, 'is a prime number.')
else:
    print(num, 'is not a prime number.')               