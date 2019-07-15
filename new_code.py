def mul(a,b):
    if a == b:
        return a**2
    return a*b

def divide(a,b):
    if b == 0:
        raise ZeroDivisionError('b can not be 0')
    else:
        return a/b
