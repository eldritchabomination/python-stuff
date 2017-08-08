
list1 = [1,2,3]
num2 = 5

def fun(obj1, obj2):
    obj1[0] = 2
    obj2 = 3

fun(list1, num2)
print 'list1', list1
print 'num2', num2