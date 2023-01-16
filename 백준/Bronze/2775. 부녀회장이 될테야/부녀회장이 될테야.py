T = int(input())

for i in range(T):
    floor = int(input())
    number= int(input())
    zero =[i for i in range(1,number+1)] 
    for k in range(floor) :
        for n in range(1,number):
            zero[n]+=zero[n-1]
    print(zero[-1])        