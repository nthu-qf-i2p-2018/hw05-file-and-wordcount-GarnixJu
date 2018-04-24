# -*- coding: utf-8 -*-
import math



def is_prime(num，prime_list=[2]):
    # your code here ...
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) +1):
        if is_prime(i,prime_list):
            if num % i == 0:
                return False
        
    return True


num = int(input("Enter a number: "))

if is_prime(num):
    print(num, 'is a prime number.')
else:
    print(num, 'is not a prime number.')