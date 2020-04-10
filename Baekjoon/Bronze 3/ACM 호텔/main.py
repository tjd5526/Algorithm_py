for _ in range(int(input())):
    H,W,N = map(int, input().split())
    print([str(j)+str(i).zfill(2) for i in range(1,W+1) for j in range(1,H+1)][N-1])
