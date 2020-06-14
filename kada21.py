def digital_root(n=456):    # 6
    # ml = sum([a for int(a)%10 in str(n)])
    while n>10:
        n = sum([int(a) for a in str(n)])
    return n
print(digital_root())