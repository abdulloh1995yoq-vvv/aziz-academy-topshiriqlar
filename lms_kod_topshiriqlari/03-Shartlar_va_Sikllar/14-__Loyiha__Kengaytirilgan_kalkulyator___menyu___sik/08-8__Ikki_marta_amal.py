import sys

data = sys.stdin.read().split()
if not data:
    sys.exit()
    
idx = 0
while idx < len(data):
    if int(data[idx]) == 0:
        print("Exit")
        break      
        
    a = int(data[idx])
    b = int(data[idx+1])
    amal = int(data[idx+2])
    idx += 3
          
    if amal == 1:
        print(a + b)
    elif amal == 2:
        print(a - b)
    elif amal == 3:
        print(a * b)
    elif amal == 4:
        print(a / b if b != 0 else 0 )