def multiply(a,b):

    res = 0
    for i in range(b):
        res += a
    
    print(res)

multiply(3,4)



def multiply(a,b):
    if b == 1:
        return a
    else:
        return a+ multiply(a,b-1)

print(multiply(3,4))