[ACM 호텔](https://www.acmicpc.net/problem/10250)
```python
for _ in range(int(input())):
    H,W,N = map(int, input().split())
    print([str(j)+str(i).zfill(2) for i in range(1,W+1) for j in range(1,H+1)][N-1])
```
그냥 모든 호텔의 방을 만들고 가져왔다.