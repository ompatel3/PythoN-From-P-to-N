print("for reusability")

def fun(a,b):
    ''' This function will return average of 2 number
    '''
    avg=(a+b)/2
    print(avg)
    return avg


print(fun.__doc__)
fun(10,30)

avrg=fun(15,45)
print(avrg)