while True:
    ans = input()
    if ans=='0':
        break
    if ans==ans[::-1]:
        print("yes")
    else:
        print("no")