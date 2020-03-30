```python
import math
a = list(map(lambda x: pow(int(x), 2), input().split()))
b = a[0]/(a[1]+a[2])
print(int(math.sqrt(b*a[1])), int(math.sqrt(b*a[2])))
```
처음 시도한 코드다
31376KB 60MS 143B

아무래도 math를 import하다보니 메모리가 좀 많이 나왔다.

```python
a = list(map(lambda x: int(x)**2, input().split()))
b = a[0]/(a[1]+a[2])
print(int((b*a[1])**0.5), int((b*a[2])**0.5))
```


```python
a, b, c = list(map(lambda x: int(x)**2, input().split()))
d = a/(b+c)
print(int((d*b)**0.5), int((d*c)**0.5))
```