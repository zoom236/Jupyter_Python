N,X = map(int,input().split())
A = list(map(int,input().split()))
A_Min = []
for i in range(N) :
    if A[i] < X :
       A_Min.append(A[i])
        
print(" ".join(str(item) for item in A_Min))