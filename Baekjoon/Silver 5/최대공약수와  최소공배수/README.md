[최대공약수와 최소공배수](https://www.acmicpc.net/problem/2609)
```python
from math import gcd
x,y = map(int,input().split())
print(gcd(x,y))
print(int(x*y/gcd(x,y)))
```

그냥 math라이브러리 불러서 gcd 해줬다.