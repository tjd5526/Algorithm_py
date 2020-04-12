[SHA-224](boj.kr/10929)
```python
import hashlib
print(hashlib.sha224(input().encode()).hexdigest())
```