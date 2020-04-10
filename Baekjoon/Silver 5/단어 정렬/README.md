[단어 정렬](https://www.acmicpc.net/problem/1181)
```python
import sys
a = set()
for _ in range(int(input())):
    a.add(sys.stdin.readline().rstrip())
a = list(a)
a.sort()
a.sort(key=len)
print("\n".join(a))
```