[세로읽기](boj.kr/10798)
```python
a = list(input().ljust(15,' '))
b = list(input().ljust(15,' '))
c = list(input().ljust(15,' '))
d = list(input().ljust(15,' '))
e = list(input().ljust(15,' '))
ans =[]
for i in range(15):
    if a[i].isspace():
        a[i]=''
    if b[i].isspace():
        b[i]=''
    if c[i].isspace():
        c[i]=''
    if d[i].isspace():
        d[i]=''
    if e[i].isspace():
        e[i]=''
    ans+=a[i]+b[i]+c[i]+d[i]+e[i]
print(''.join(ans))
```