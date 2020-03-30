a, b, c = map(lambda x: int(x)**2, input().split())
d = a/(b+c)
print(int((d*b)**0.5), int((d*c)**0.5))