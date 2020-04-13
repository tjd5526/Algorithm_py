[X보다 작은수](boj.kr/10871)
```python
_, x = map(int, input().split())
ans = list(map(int, input().split()))
print(*[i for i in ans if i<x])
```