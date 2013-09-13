# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 12:27:15 2013

@author: lucab0ni

Problem 3 - Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""

import time
import array

start_time = time.time()

startValue = 600851475143
highestPrime = 1
mul = 1

primeList = array.array('i')
primeList.append(2)

for x in range(2, 10000):
    if not(startValue % x):
        startValue = startValue / x
        highestPrime = x
        mul *= highestPrime
        print "new prime factor found ", x
        print "multiplication = ", mul

    if mul == 600851475143:
        break


print "Execution time:", time.time() - start_time, "[s]"
print "The answer is ", highestPrime

# 6857
