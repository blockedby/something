def is_square(n):    
    if n<0:
        return False
    if n==0:
        return True
    if n.__divmod__(n)==[n**(1/2),0]:
        return True
ab = 1
ab.__divmod__()