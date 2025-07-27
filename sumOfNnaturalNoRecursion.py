def sumn(sum,i,n):
    if i > n:
        print(sum)
        return
    sumn(sum+i,i+1,n)
sumn(0,1,4)