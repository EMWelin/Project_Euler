"""
Euler Project 007 find n primes.

https://www.hackerrank.com/contests/projecteuler/challenges/euler007/problem?isFullScreen=true

I need to look through n * (ln(n) + ln(ln(n)) numbers and find atleast n primes.

If we have the bound we can use the Sieve of Eratosthenes algorithm
to find all primes below the bound because we know how many numbers to check.

It's also possible to use 'Dynamic Sieve' algorithm to generate the n first primes.
No bound needed in that case.

"""

# Erik Martin Welin
# 2025-05


"""
upper_bound_for_n_primes(n):
given that we are looking for n primes,
return the number of natural integers we have to look through
in order to guarantee that we find n primes.
"""

def upper_bound_for_n_primes(n):
    
    if n < 6:
        return 15  # hardcoded since formula underestimates here
    return math.ceil(n * (math.log(n) + math.log(math.log(n))))


"""
sieve_of_eratosthenes(n): 
find all primes <= n
"""

def sieve_of_eratosthenes(n):
  
  arr = (n+1) * [True]
  arr[0] = False
  arr[1] = False

  # isqrt: integer square root.

  upper_limit = math.isqrt(n) +1
  for i in range(2, upper_limit):
  
    if arr[i]:
      for m in range(i*i, n+1, i):
          # mark as not prime
          arr[m] = False
          
  # return those numbers not marked as 0 i.e. the prime ones.    
  # enumerate creates tuple (index, value)  

  primes = [i for i, prime in enumerate(arr) if prime]
  
  return primes
