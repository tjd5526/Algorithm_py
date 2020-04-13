import sys
n, m = map(int, sys.stdin.readline().split())
ans = []
nolis = dict()
for i in range(n):
    name = sys.stdin.readline().rstrip()
    nolis[hash(name)]=None
for j in range(m):
    name = sys.stdin.readline().rstrip()
    if hash(name) in nolis:
        ans.append(name)
ans.sort()
print(len(ans))
for i in ans:
    print(i)