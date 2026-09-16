import sys 

input_deta = sys.stdin.read().split()
if input_deta:
    a = int(input_deta[0])
    b = int(input_deta[1])
    print(a % b)