import sys 

input_deta = sys .stdin.read().split()

if len(input_deta) >= 2:
    a = int(input_deta[0])
    b = int(input_deta[1])
    
    if b == 0:
        print("Error")
    else:
        print(a / b)