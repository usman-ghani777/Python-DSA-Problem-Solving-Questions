num = 23456
noD = len(str(num))
total = 0
temp = num  # Preserve original number

while temp > 0:
    last_digit = temp % 10
    total += last_digit ** noD  # use += to accumulate
    temp //= 10  # reduce the number

print(total)

# Optional check if Armstrong number
if total == num:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
