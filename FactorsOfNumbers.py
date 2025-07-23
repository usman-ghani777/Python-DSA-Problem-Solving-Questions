num = 20
result = []

for i in range(1,(num+1)//2):
    if num%i == 0:
        result.append(i)
        
result.append(num)
print(result)