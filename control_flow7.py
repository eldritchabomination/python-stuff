def f(a, L=None):
    if L is None:
        print L
        L = []
    L.append(a)
    return L