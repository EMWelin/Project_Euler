"""
Euler Project 003
https://www.hackerrank.com/contests/projecteuler/challenges/euler003/problem?isFullScreen=true

This function returns the greatest prime factor of N
My solution also calculates a list of all prime factors of n because, why not?

Relevant knowledege:

1. Fundamental Theorem of Arithmetic.

In mathematics, the fundamental theorem of arithmetic, also called the unique factorization theorem and prime factorization theorem,
states that every integer greater than 1 can be represented uniquely as a product of prime numbers, up to the order of the factors // Wikipedia.

Relevance: This tells us to look for prime factors amongst the integers. It also guarantees that the code will sucessfully come up with a factorisation.
Furthermore, it guarantees that the factorisation is unique up to the order of the factors (i.e. 2 * 5 is equivalent to 5 * 2). 

2. If an integer n = a * b then it follows that:

a < sqrt(n) < b

A number cannot have more than one distinct prime-factor larger than sqrt(n)

Relevance: This gives us a restriction on where to search for prime factors for a number n.

3. If p is a prime factor of n and p^2 > n then p is the largets prime factor of n

Relevance: This is used as an exit condition in the code.

"""

import math
import copy

# Erik Martin Welin
# 2025-05

def greatest_prime_factor(N):


  n = copy.deepcopy(N)

  prime_factors = []

  # start by dividing out 2's.
  # that allows me to check 3,5,7,9,11,13,15,17 etc later

  while n%2 == 0:
      n = n//2
      prime_factors.append(2)

  # check if N is 2^m

  if n == 1:
    return 2 


  # divide out odd primes. 

  def divide_out_primes(N):
    
    upper_limit = math.floor(math.sqrt(N))
    for i in range(3, upper_limit +1, 2):
      if N % i == 0:
        return N//i, i
    
    # no divisors found

    return N, None


  while True:

    n, factor = divide_out_primes(n)
    if factor == None:
      # n is prime
      prime_factors.append(n)
      break
    
    # else, append the found factor and keep going.
    prime_factors.append(factor)

    # This is point 3 in the introduction
    # if this condition is met, we have the largest prime factor.
    
    if pow(factor, 2) > n:
      prime_factors.append(n)
      break

  return max(prime_factors)
