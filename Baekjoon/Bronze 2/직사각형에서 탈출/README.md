[직사각형에서 탈출](https://www.acmicpc.net/problem/1085)
```python
a, b, c, d = map(int, input().split())
print(min(c-a,d-b,a,b))
```