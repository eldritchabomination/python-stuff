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

def ask_ok(prompt, retries=4, complaint="Yes or no"):
    """Asks the user to input a yes or no value."""
    while True:
        ok = raw_input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise IOError('refusenik user')
        print complaint
