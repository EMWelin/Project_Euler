import sys

data = list(map(int, sys.stdin.read().split()))
inputs = data[1:]

print(str(sum((x for x in inputs)))[:10])
