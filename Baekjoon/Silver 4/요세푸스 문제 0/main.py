c,b=map(int,input().split())
a=list(range(1,c+1))
result = []
temp = b-1

for i in range(1,c+1):
    if len(a)>temp:
        result.append(a.pop(temp))
        temp+=b-1
    elif len(a)<=temp:
        temp%=len(a)
        result.append(a.pop(temp))
        temp+=b-1
result=list(map(str,result))
print('<'+", ".join(result)+">")