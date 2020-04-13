[~](boj.kr/10886)
```python
ans = [input() for i in range(int(input()))]
if ans.count('0')>ans.count('1'):
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")
```