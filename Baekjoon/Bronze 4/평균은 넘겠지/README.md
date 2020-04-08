[평균은 넘겠지](https://www.acmicpc.net/problem/4344)
```python
[print("{:.3f}%".format(sum([1 for j in i[1:] if j>sum(i[1:])/i[0]])/i[0]*100)) for i in [list(map(int,input().split())) for _ in range(int(input()))]]
```