[직각삼각형](boj.kr/4153)
```python
import sys

while True:
    a = sorted(map(int,sys.stdin.readline().split()))
    if 0 in a:
        break
    if (a[0]**2+a[1]**2)**0.5==a[2]:
        print("right")
    else:
        print("wrong")
```