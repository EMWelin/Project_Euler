"""
Project_Euler 002, Even Fibonacci Numbers

https://www.hackerrank.com/contests/projecteuler/challenges/euler002/problem?isFullScreen=true

Fiboniacci sequence:=
F_N = F_N-1 + F_N-2

For this particular problem:
F_0 = 1
F_1 = 2

1, 2, 3, 5, 8, 13, 21, 34, 55, 89...
"""

# Erik Martin Welin 
# 2025-05


def sum_even_fibonacci(n):
  
    fib_list = []
    fib_list.append(1)
    fib_list.append(2)

    for i in range(2, n):
      fib_val = fib_list[i-1] + fib_list[i-2]
      if fib_val >= n:
        break
      fib_list.append(fib_val)

    return sum(list(x for x in fib_list if x%2 == 0 and x <= n))
