X = int(input())
N = int(input())
temp = []
for i in range(N) :
    a,b = map(int,input().split())
    price = a*b
    temp.append(price)

total = 0    
for i in range(len((temp))) :
    total += temp[i]

if X == total :
    print('Yes')
else :
    print('No')
    