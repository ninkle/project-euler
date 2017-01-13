#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 14:14:24 2017

@author: nicolefitzgerald
"""

#PROBLEM3: What is the largest prime factor of the number 600851475143 ?
def primeFactorization(n):
    factors = []
    divisor = 2        
    while n > 1:        
        while n % divisor == 0:
            factors.append(divisor)
            n /= divisor          
        divisor = divisor + 1
        if divisor*divisor > n:
            if n > 1: 
                factors.append(n)
            break
    return factors
    

theFactors = primeFactorization(600851475143)
print(theFactors[-1])
