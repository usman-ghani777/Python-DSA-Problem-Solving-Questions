# Head recursion
def func(x, n):
    if n == 0:    # stop when n reaches zero
        return
    print(x)
    func(x, n - 1)

func(5, 4)

# Tail Recu^rsion

def func2(x,n):

    if n==0:
        return
    func2(x,n-1)
    print(x)
func2(3,4)
