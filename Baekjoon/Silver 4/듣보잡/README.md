[듣보잡](boj.kr/1764)
```python
import sys
n, m = map(int, sys.stdin.readline().split())
ans = []
nolis = dict()
for i in range(n):
    name = sys.stdin.readline().rstrip()
    nolis[hash(name)]=None
for j in range(m):
    name = sys.stdin.readline().rstrip()
    if hash(name) in nolis:
        ans.append(name)
ans.sort()
print(len(ans))
for i in ans:
    print(i)
```
set으로 푸는 방법다음으로 메모리를 적게 먹는다. 33920 vs 33992