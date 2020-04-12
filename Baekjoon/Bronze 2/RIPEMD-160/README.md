[RIPEMD-160](boj.kr/10933)
```python
import hashlib
ans = hashlib.new("ripemd160")
ans.update(input().encode())
print(ans.hexdigest())
```

hashlib.new를 했을때 OpenSSL에서 사용가능한 다른 알고리즘을 쓸 수 있다.