"""
Project Euler 004
https://www.hackerrank.com/contests/projecteuler/challenges/euler004/problem?isFullScreen=true

"Find the largest palindrome made from the product of two 3-digit numbers which is less than N"
143 * 707 being the smallest palindrome with 3-digit factors is given in the problem and used in the solution.

This one requires a brute force solution because there is no clever way
to generate palindromical numbers. The problem is about optimising the process.


# the two main timesavers:

1. We are looking for largest product so going downwards from 999 to 100
is most effecient. As a,b, is montonically declining we can break when a*b < current_max_prod

2. a*b = b*a. This means that we can start the b loop at a. We don't have to check a * b and b * a.

Example:
Outer loop: a == 999
Inner loop: b: 999, 998,...100
After this we have checked all combinations of 999 so starting b at 999 in the next iteration of a is a waste of time. Instead we start at a.
"""

# Erik Martin Welin
# 2025-05

def is_palindrome(n):
  s = str(n)
  return s == s[::-1]
  


if __name__ == '__main__':
    t = int(input().strip())
    

    
    for t_itr in range(t):
        n = int(input().strip())
        
        # smallest palindrome number made up of 3 digit factors = 143*707
        max_value = 143 * 707 


        for a in range(999, 99,-1):
            for b in range(a, 99, -1):
        # save a*b because we reuse the result
                product = a*b
                if product < max_value:
                    break
                if is_palindrome(product) and n > product:
                    max_value = product
                    
        print(max_value)
