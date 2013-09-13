# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 09:55:49 2013

@author: lucab0ni

Problem 1 - Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

"""

import time

start_time = time.time()

sum = 0

for x in range(1, 1000):
    if not(x % 3) or not(x % 5):
        sum += x

print "Execution time:", time.time() - start_time, "[s]"
print "The answer is ", sum

# 233168