def func(s,l,r):
    if l>=r:
        return True
    if s[l]!=s[r]:
        return False
    return func(s,l+1,r-1)

ss ="mom"
left = 0
right = len(ss) - 1
print(func(ss,left,right))


