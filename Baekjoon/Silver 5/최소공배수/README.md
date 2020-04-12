[최소공배수](boj.kr/1934)
```python
import math, sys

for i in range(int(input())):
    a,b = map(int, sys.stdin.readline().split())
    print(a*b//math.gcd(a,b))
```