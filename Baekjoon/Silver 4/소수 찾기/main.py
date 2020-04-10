n = int(input())
m = list(map(int, input().split()))
a=set(range(3,1000,2))
for i in range(3,1000,2):
    if i in a:
        a-=set(range(i*2,1000,i))
num2 = 0
if 2 in m:
    num2+=1
print(sum([1 for i in range(len(m)) if m[i] in a])+num2)