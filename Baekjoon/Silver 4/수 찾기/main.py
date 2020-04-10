def binsearch(arr, val, low, high):
    if low > high:
        return False

    mid = (low + high) // 2
    if arr[mid] > val:
        return binsearch(arr, val, low, mid - 1)
    elif arr[mid] < val:
        return binsearch(arr, val, mid + 1, high)
    else:
        return True


N = int(input())
ans = sorted(list(map(int, input().split())))
input()
chk = list(map(int, input().split()))

for m in chk:
    if binsearch(ans, m, 0, N - 1):
        print(1)
    else:
        print(0)