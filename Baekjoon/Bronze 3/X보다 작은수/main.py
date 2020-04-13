_, x = map(int, input().split())
ans = list(map(int, input().split()))
print(*[i for i in ans if i<x])