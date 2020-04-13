A,B,C = int(input()),int(input()),int(input())
ans=list(map(int,str(A*B*C)))
for i in range(10):
    print(ans.count(i))
