remainder = []
for i in range(10):
    A = int(input()) % 42
    remainder.append(A)
    
print(len(set(remainder)))