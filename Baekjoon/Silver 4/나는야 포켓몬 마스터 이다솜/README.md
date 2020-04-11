[나는야 포켓몬 마스터 이다솜](https://www.acmicpc.net/problem/1620)
```python
import sys

a,b = map(int, sys.stdin.readline().rstrip().split())

ans = dict(zip(range(1,a+1),[sys.stdin.readline().rstrip() for _ in range(a)]))
ans2 = {v:k for k,v in ans.items()}
chk = [sys.stdin.readline().rstrip() for _ in range(b)]

for i in chk:
    if i.isdigit():
        print(ans[int(i)])
    else:
        print(ans2[i])
```