a, b = input().split()
a = int(a)
b = int(b)
amal = input().strip()

if amal == "add":
    print(a + b)
elif amal == "sub":
    print(a - b)
elif amal == "mul":
    print(a * b )
elif amal == "div":
    print(a / b if b != 0 else 0)