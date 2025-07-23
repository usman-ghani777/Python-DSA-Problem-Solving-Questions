num = [1,2,3,1,2,5,4,3,2,6,7,7,7]
dic = dict()
for i in num:
    if num[i] in dic:
        dic[num[i]]+=1
    else:
        dic[num[i]] = 1
print(dic)

#***************#(More optimal Code)#***************************

num2 = [3,4,5,1,2,34,5,6,3,3]
dic2 = dict()
for j in range(0,len(num2)):
    dic2[num[j]] = dic2.get(num[j],0)+1
print(dic2)