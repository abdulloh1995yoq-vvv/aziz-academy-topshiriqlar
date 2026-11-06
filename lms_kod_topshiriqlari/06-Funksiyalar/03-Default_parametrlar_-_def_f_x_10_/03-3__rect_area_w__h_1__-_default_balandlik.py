def rect_area(w, h=1):
    return w*h
d = list(map(int, input().split()))
print(rect_area(*d))