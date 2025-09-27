nums = [19, 2, 4, 9, 3, 5, 8, 10]
n = len(nums)

ans = [-1] * n
stack = []   # <-- define the stack

for i in range(n-1, -1, -1):   # traverse from right to left
    while stack and stack[-1] <= nums[i]:
        stack.pop()

    if stack:
        ans[i] = stack[-1]

    stack.append(nums[i])

print(ans)
