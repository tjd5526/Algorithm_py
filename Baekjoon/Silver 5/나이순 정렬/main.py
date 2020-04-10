import sys
ans=[]
for _ in range(int(input())):
    ans.append(sys.stdin.readline().split())
for i in sorted(ans,key=lambda x:int(x[0])):
    print(' '.join(i))