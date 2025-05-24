"""
Euler Project 006

https://www.hackerrank.com/contests/projecteuler/challenges/euler006/problem?isFullScreen=true

Find the absolute difference between 
the sum of the squares of the first  natural numbers and the square of the sum.
"""

# Erik Martin Welin 
# 2025-05

def abs_difference(n):
    
    nat_numbers = list(range(0,n+1))
    nat_squares = sum(pow(x,2) for x in nat_numbers)
    nat_sum = pow(sum(nat_numbers), 2)
    return abs(nat_sum - nat_squares)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())
        print(abs_difference(n))
