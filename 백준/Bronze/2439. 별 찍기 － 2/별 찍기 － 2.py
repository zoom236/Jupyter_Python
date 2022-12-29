n = int(input())

for i in range(n) :
    space = n-i-1
    if space == 0 :
        print("*"*(i+1))
    else :
        print(" "*(n-i-2),"*"*(i+1))