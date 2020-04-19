for i in range(int(input())):
    a,b,c,d,e,f,g,h = map(int,input().split())
    hp = a+e
    mp=b+f
    atk=c+g
    dfs=d+h
    if hp<1:
        hp=1
    if mp<1:
        mp=1
    if atk<0:
        atk=0
    print(1*hp+5*mp+2*atk+2*dfs)
