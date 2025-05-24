"""
Project Euler 8
https://www.hackerrank.com/contests/projecteuler/challenges/euler008/problem?isFullScreen=true
"""

# Erik Martin Welin
# 2025-05

def max_prod_len_k(k, num):

  s = str(num)
  max_prod = 0

  for i in range(0, len(s) -k):
    prod = int(s[i])
    for m in range(1, k):
      prod = prod * int(s[i+m])
    if prod > max_prod:
      max_prod = prod
  
  return max_prod
