"""
Project Euler 005
https://www.hackerrank.com/contests/projecteuler/challenges/euler005/problem?isFullScreen=true

This problem is looking for LCM(1,2,3....N) inclusive
for 1 <= N <= 40

My solution makes use of:

(1) lcm(a,b) = abs(a) * abs(b) / GCD(a,b) = /a > 0, b > 0/
a * b / GCD(a,b)   

It also makes use of the following:

(2) if a_1, a_2, ... a_m all are non-zero then:
  lcm(a_1:a_m) = lcm( lcm(a_1:a_m-1), a_m ) (2)

What (2) says is that we can apply the formula in (1) iteratively.

functools.reduce can be used to apply a function iteratively. 
Syntax: reduce(function, iterable[, initializer])
"""

# Erik Martin Welin
# 2025-05

import math
from functools import reduce

# This functon computes the least common multiple of a,b
# this one only works for a*b > 0

def lcm_positive(a,b):
  return a * b // math.gcd(a,b)


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        lcm = reduce(lcm_positive, list(x for x in range(1, n+1)))
        print(lcm)
