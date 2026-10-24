def calc_all(a,b,c):
    return a+b+c, a*b*c, max(a,b,c), min(a,b,c)
a,b,c = map(int, input().split())
print("pos:", *calc_all(a,b,c))
print("named:", *calc_all(c=c, b=b, a=a))