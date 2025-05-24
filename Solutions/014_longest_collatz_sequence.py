"""
Euler Project 014

https://www.hackerrank.com/contests/projecteuler/challenges/euler014/problem?isFullScreen=true

Theory: 

The Collatz sequence is a sequence defined for positive integers.

n --> n / 2 if n is even
n --> 3n +1 if n is odd

Collatz Conjecture :=

The Collatz Conjecture states that every positive integer eventually reaches 1
which leads to the loop 4,2,1. This conjecture is considered likely impossible
to prove given the current state of collective mathematical knowledge.

"""

# This submission passed 8 / 12 test cases and timed out in the remaining 4.
# I don't know how to optimise further.

# Erik Martin Welin 2025-05

import sys


# memo[key] says how many steps are needed to from key to 1.
# This dict is used to remember previously computed paths.


memo = {}
memo[1] = 0

def collatz(N, memo):

    n = N
    path = [n]  # start path with original N
    steps = 0

    while True:
        if n in memo:
            final_steps = steps + memo[n]
            # Update memo for all visited numbers
            for i, val in enumerate(path):
                memo[val] = final_steps - i
            return final_steps

        steps += 1
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        path.append(n)


    
# read inputs.
    
data = list(map(int, sys.stdin.read().split()))
T = data[0]
inputs = data[1:]
N_max = max(inputs)

    
max_steps = 1
longest_sequence = 0
best = [0] * (N_max +1)
best[1] = 1

# precompute longest sequence for all N.
# computing for 1,2,3.. 10 (for example)
# and then computing for 1,2,3... 15 is a waste of time because we've already done the calculation for <= 10 previously.
# It's better to compute the answer for all <= N and then do a list lookup for the test cases.

for i in range(2, N_max + 1):
        
    steps = collatz(i, memo)
    if steps >= max_steps:
        max_steps = steps
        longest_sequence = i
            
    best[i] = longest_sequence  

# output longest_sequence for all n <= N_i, testcase i.

for val in inputs:
    print(best[val])
