n = int(input())
list_n = list(map(int,input()))
sum = 0
for i in range(n) :
    sum += list_n[i-1]
print(sum)