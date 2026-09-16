import sys 

input_deta = sys.stdin.read().split()
if len(input_deta) >= 2:
    a = int(input_deta[0])
    b = int(input_deta[1])
    
    if a < 0 or b < 0:
        print("Invalid")
    else:
        print(a + b)