# Tail Recursion
def func(count = 0):
 
    if count == 4:
        return
    func(count + 1)
    print("usman")
func()