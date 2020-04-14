[TGN](boj.kr/5063)
```python
import sys
for i in range(int(input())):
    r,e,c = map(int, sys.stdin.readline().split())
    if r<e-c:
        print("advertise")
    elif r==e-c:
        print("does not matter")
    else:
        print("do not advertise")
```