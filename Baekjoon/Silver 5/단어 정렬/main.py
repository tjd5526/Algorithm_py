import sys
a = set()
for _ in range(int(input())):
    a.add(sys.stdin.readline().rstrip())
a = list(a)
a.sort()
a.sort(key=len)
print("\n".join(a))