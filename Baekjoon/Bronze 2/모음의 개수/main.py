import sys
while True:
    a = sys.stdin.readline().rstrip().lower()
    if a=="#":
        break
    print(sum(map(lambda x : a.count(x), 'aeiou')))
