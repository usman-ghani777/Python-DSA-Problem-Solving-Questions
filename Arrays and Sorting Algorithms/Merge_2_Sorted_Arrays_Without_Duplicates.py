num1 = [1, 1, 1, 2, 3, 4, 5, 6]
num2 = [1, 2, 3, 4, 5, 6, 7]
result = []

i = 0
j = 0
n1 = len(num1)
n2 = len(num2)

while i < n1 and j < n2:
    if num1[i] < num2[j]:
        if len(result) == 0 or result[-1] != num1[i]:
            result.append(num1[i])
        i += 1
    elif num2[j] < num1[i]:
        if len(result) == 0 or result[-1] != num2[j]:
            result.append(num2[j])
        j += 1
    else:  # num1[i] == num2[j]
        if len(result) == 0 or result[-1] != num1[i]:
            result.append(num1[i])
        j += 1

while i < n1:
    if len(result) == 0 or result[-1] != num1[i]:
        result.append(num1[i])
    i += 1

while j < n2:
    if len(result) == 0 or result[-1] != num2[j]:
        result.append(num2[j])
    j += 1

print(result)
