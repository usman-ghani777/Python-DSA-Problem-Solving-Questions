num = int(input("Enter the Number to Check:"))
orignal = num # Save the original number
rev = 0
while num > 0:
    
    last_digit = num%10
    print(last_digit)
    rev = rev * 10 + last_digit  
    num = num//10  # division by 10 decrement the last_digit

if orignal == rev:
    print(f"your {orignal} is a palindrome")
else:
    print(f"your {orignal} is not a palindrome")


  

