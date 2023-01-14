import math
T = int(input())
f = 0
r = 0
for i in range(T):
    H,W,N = map(int,input().split())
    r = math.ceil(N/H)
    if H<N :
        f = N-H*(N//H)
        if f == 0 :
            f = H
    else :
        f = N 
    print("%01d%02d" %(f,r))