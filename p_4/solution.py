# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 13:20:10 2013

@author: lucabonifacio

Problem 4 - Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""

import time

start_time = time.time()

highestValue = 0

def verify(value):
    isValid = True
    valueToStr = str(value)
    if not(len(valueToStr) % 2):
        for x in range(len(valueToStr) / 2):
            if valueToStr[x] != valueToStr[len(valueToStr) - 1 - x]:
                isValid = False
                break
    return isValid

for x in range(100, 999):
    for y in range(100, 999):
        if verify(x * y) == True:
            if highestValue < (x * y):
                highestValue = x * y


print "Execution time:", time.time() - start_time, "[s]"
print "The answer is", highestValue

# 906609