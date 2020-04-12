[SHA-512](boj.kr/10932)
```python
import hashlib
print(hashlib.sha512(input().encode()).hexdigest())
```