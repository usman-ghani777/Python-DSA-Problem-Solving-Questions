num = 986754321
rev = 0
while num > 0:
    
    last_digit = num%10
    print(last_digit)
    rev = rev * 10 + last_digit  
    num = num//10  # division by 10 decrement the last_digit

print(rev)


  

