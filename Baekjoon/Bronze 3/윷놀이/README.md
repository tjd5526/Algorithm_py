[윷놀이](boj.kr/2490)
```python
import sys
ans = ["D","C","B","A","E"]
for i in range(3):
    chk = sum(map(int, sys.stdin.readline().split()))
    print(ans[chk])
```