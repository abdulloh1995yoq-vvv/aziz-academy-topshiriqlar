import sys

deta = sys.stdin.read().split()

if len(deta) >= 3:
    a = int(deta[0])
    b = int(deta[1])
    choise = int(deta[2])
    
    if choise == 1:
        print(a + b)