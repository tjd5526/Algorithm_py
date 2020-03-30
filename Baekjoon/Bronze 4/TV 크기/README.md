```python
import math
a = list(map(lambda x: pow(int(x), 2), input().split()))
b = a[0]/(a[1]+a[2])
print(int(math.sqrt(b*a[1])), int(math.sqrt(b*a[2])))
```
처음 시도한 코드다.

31376KB 60MS 143B

아무래도 math를 import하다보니 메모리가 좀 많이 나왔다.

```python
a = list(map(lambda x: int(x)**2, input().split()))
b = a[0]/(a[1]+a[2])
print(int((b*a[1])**0.5), int((b*a[2])**0.5))
```
두번째 코드다.
math.sqrt 대신 **0.5로 바꿔주고 pow대신 **2로 바꿔줬다.
29284KB 60MS 118B

```python
a, b, c = map(lambda x: int(x)**2, input().split())
d = a/(b+c)
print(int((d*b)**0.5), int((d*c)**0.5))
```
세번째 코드다.
리스트 대신 변수를 사용했다.
29284KB 56MS 103B