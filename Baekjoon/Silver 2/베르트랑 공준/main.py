import sys
while True:
    count = 0
    a=int(sys.stdin.readline().rstrip())
    if a==0:
        break
    if a<=2:
        count+=1
    asdf = set(range(3,a*2+1,2))
    for i in range(3,a*2,2):
        if i in asdf:
            asdf-=set(range(i*2,a*2+1,i))
    asdf-=set(range(3,a+1,2))
    if a==3:
        asdf.add(3)
    count+=len(asdf)
    print(count)