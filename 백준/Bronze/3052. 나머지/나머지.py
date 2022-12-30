temp = []
for i in range(10):
    num = int(input())
    remainder = num % 42
    temp.append(remainder)
temp =set(temp)
print(len(temp))