num = 56789
print(type(num)) # int type
count = 0

while num > 0:
    
    num = num//10 # division by 10 decrement the last_digit 
    count+=1 # increment count with every iteration

print(count)


