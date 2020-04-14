import sys
chk = {int(sys.stdin.readline()):i for i in range(1,9)}
ans = sorted(chk)
print(sum(ans[3:]))
print(' '.join(sorted([str(chk[j]) for j in ans[3:]])))