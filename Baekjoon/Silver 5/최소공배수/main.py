import math, sys

for i in range(int(input())):
    a,b = map(int, sys.stdin.readline().split())
    print(a*b//math.gcd(a,b))