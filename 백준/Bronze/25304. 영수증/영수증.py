X = int(input())
N = int(input())
for i in range(N) :
    a,b = map(int, input().split())
    X = X-(a*b)
    
print('Yes') if X == 0 else print('No')