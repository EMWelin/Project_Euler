"""
Project Euler 009
https://www.hackerrank.com/contests/projecteuler/challenges/euler009/problem?isFullScreen=true

Problem formulation:

Given N, Check if there exists any Pythagorean triplet for which a+b+c == N
Find maximum possible value of  among all such Pythagorean triplets,
If there is no such Pythagorean triplet print -1.


Necessary theory:

A pythagorean triple consists of positive integers a,b,c such that

a^2 + b^2 = c^2

Euclid's method of generating triplets:

a,b,c form a triplet when they are chosen as:

a = m^2 - n^2 
b = 2mn 
c = m^2 + n^2

for integers m,n that satisfies m > n > 0

Definition: Primtive triplets.

If a < b < c satisfies:
a^2 + b^2 = c^2 and
GCD(a,b,c) = 1 (i.e. they are coprime)
then abc form a primitive triplet.


Useful theorem:

It can be shown that a,b,c will form a primitive triplet when exactly one of
m, n is even, GCD(a,b) == 1 and m > n.


The concept of primitive triplets is important because
if a,b,c is a triplet then ka, kb, kc is also a triplet for integer k > 0.
This means that the primitive triplets can generate the non-primitive triplets.
"""


# Erik Martin Welin 2025-05


# this function:
# return max(a*b*c) such that a + b = c = N and a,b,c is a pythagorean triplet.


def special_triplets(N):

  triplets = []

  # this bound for m is based on k*(a+b+c) <= N
  # substitute to get function of m and n and
  # evaluate at k = 1 and n = 1 to get safest possible bound.

  m_bound = int( -1/2 + math.sqrt( (2*N+1)/4 ))
  
  for m in range(2, m_bound + 1):
    for n in range(1, m):  # loop til m-1 to ensure m > n

      if math.gcd(m,n) == 1 and (m-n)%2 == 1:

        a = pow(m, 2) - pow(n,2)
        b = 2*m*n
        c = pow(m,2) + pow(n,2)

        # generate new triplets from a,b,c using the free paramter k
        
        k = 1
        while True:
          perimeter = k*(a+b+c)
          if perimeter == N:
            triplets.append((k*a,k*b,k*c))

          if perimeter > N:
            break  
          # if no break, increment k
          k += 1 

  if len(triplets) == 0:
    return -1
  return max( a*b*c for a,b,c in triplets )
