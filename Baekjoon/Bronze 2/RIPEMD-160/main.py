import hashlib
ans = hashlib.new("ripemd160")
ans.update(input().encode())
print(ans.hexdigest())