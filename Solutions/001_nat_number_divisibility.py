
"""
Project Euler problem 001

https://www.hackerrank.com/contests/projecteuler/challenges/euler001/problem?isFullScreen=true

Sum all the nautral numbers <N that are multiples of 3 or 5.

My comment: if I define N-sized arrays or do for loops the code runs too slow.
I need to use math knowledge.

My solution is based on:

sum multiples of k less than n =

i = (n-1) //k
sum k *i    = / variable change/
i = 1

    i = m
k * sum i  = k * m (m+1) / 2
    i = 1

"""



# Erik Martin Welin
# 2025-05


# sum multiples of k less than n

def sum_multiples_of_k(k,n):

  m = (n-1)//k

  return k * m * (m+1) // 2

# sum all natural numbers divisble by 3 or 5
# need to substract divisble by 15 because they get counted twice

def nat_sum(n):

  sum_3 = sum_multiples_of_k(3,n)
  sum_5 = sum_multiples_of_k(5,n)
  sum_15 = sum_multiples_of_k(15,n)

  return sum_3 + sum_5 -sum_15
  
