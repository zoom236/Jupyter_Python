Test = int(input())

for case in range(Test) :
    a,b = input().split()
    for i in range(len(b)):
        print(b[i]*int(a), end = '')
    print() 
    