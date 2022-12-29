import sys

T = int(input())
sum = []
for i in range(T) :
    a,b = map(int,sys.stdin.readline().split())
    add = a+b
    sum.append(add)

for i in range(len(sum)):
    print(sum[i])