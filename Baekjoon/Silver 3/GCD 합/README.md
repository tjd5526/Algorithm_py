[GCD 합](boj.kr/9613)
```python
import math, sys

for i in range(int(input())):
    ans = 0
    a = list(map(int, sys.stdin.readline().split()))
    for j in range(1,a[0]+1):
        for k in range(1+j,a[0]+1):
            ans+=math.gcd(a[j],a[k])
    print(ans)
```