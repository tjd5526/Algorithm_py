[팰린드롬수](boj.kr/1259)
```python
while True:
    ans = input()
    if ans=='0':
        break
    if ans==ans[::-1]:
        print("yes")
    else:
        print("no")
```