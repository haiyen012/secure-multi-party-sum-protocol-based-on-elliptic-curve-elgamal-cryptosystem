# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 11:18:54 2023

@author: Yen Nguyen Hai
"""
import random

random.seed(11201)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True



def rand_prime():
    primes = []
    for num in range(2, 1000):
        if is_prime(num):
            primes.append(num)
            
    return random.choice(primes)


def to_hex(curve_point):
    print(f"x = {hex(curve_point.x)} and y = {hex(curve_point.y)}")
