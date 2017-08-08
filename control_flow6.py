def func(a=[]):
    if len(a) == 0:
        a.append(1)
        print 1
        return 1
    else:
        print 0
        return 0

def fun(f=func()):
    print f
    
fun()
fun()