n, chk = map(int, input().split())
che = set(range(2,n+1))
ans = 0
for i in range(2,n+1):
    delche = set()
    if i in che:
        for j in range(i, n+1, i):
            if j in che:
                ans += 1
                delche.add(j)
            if ans == chk:
                print(j)
                break
        che-=delche
    if ans==chk:
        break