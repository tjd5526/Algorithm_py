[알람 시계](https://www.acmicpc.net/problem/2884)
```python
a,b = map(int, input().split())

if a==0 and b<45:
    a+=24
b=a*60+b-45
a=b//60
b%=60
print(a,b)
```