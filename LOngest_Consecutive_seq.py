# nums = [1, 99, 101, 98, 2, 5, 3, 4, 100, 102, 103]
# max_ = 0

# for i in range(len(nums)):
#     num = nums[i]
#     count = 1
#     while num + 1 in nums:
#         count += 1
#         num += 1
#     max_ = max(max_, count)

# print(max_)
#****************************************************

# nums = [1,1,1,2,5,98,99,100,101]
# nums.sort()
# count = 0
# last_smaller = float('inf')
# longest = 0
# for i in range(0,len(nums)):
#     num  = nums[i]
#     if num-1 == last_smaller:
#         count+=1
#         last_smaller = num
#     elif num!= last_smaller:
#         count = 1
#         last_smaller = num
#     longest = max(longest,count)
# print(longest)
#**************************************************************************

nums = [1,99,101,98,2,5,3,100,1,1]
my_set  = set()

for i in range(0,len(nums)):
    my_set.add(nums[i])

longest = 0

for num in my_set:
    if num-1 not in my_set:
        x = num
        count = 1
        while num+1 in my_set:
            count+=1
            x+=1
        longest = max(longest,count)
print(longest)



