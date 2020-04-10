[나이순 정렬](https://www.acmicpc.net/problem/10814)
```python
import sys
ans=[]
for _ in range(int(input())):
    ans.append(sys.stdin.readline().split())
for i in sorted(ans,key=lambda x:int(x[0])):
    print(' '.join(i))
```