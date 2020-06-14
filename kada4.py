# Test.assert_equals(iq_test("2 4 7 8 10"),3)
# Test.assert_equals(iq_test("1 2 2"), 1)
# Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.

# ! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)

# ##Examples :

# iq_test("2 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even

# iq_test("1 2 1 1") => 2 // Second number is even, while the rest of the numbers are odd
test1 = "2 4 7 8 10" # 3
test2 = "1 2 2" # 1
test3 = "5 5 11 13 17 6" # 6
test4 = "1 3 4 5" # 3
# testnum = 1
# for x in test1.split(' '):
#     chet = [0,0]
#     nechet = [0,0]
#     # int(x, base=10).__divmod__(2)[1] остаток от деления
#     if int(x, base =10).__divmod__(2)[1].__eq__(0):
#         chet[0] += 1
#         chet[1] += 1
#     else:
#         nechet[0] += 1
#         nechet[1] += 1


def my(string):
    c = 1
    chet = [0,c]
    nechet = [0,c]
    while not ((chet[0])>=2 and nechet[0]==1 or nechet[0]>=2 and chet[0]==1):
    # while not ((chet[0].__ge__(2).__and__(nechet[0].__eq__(1))) or (nechet[0].__ge__(2).__and__(chet[0].__eq__(1)))):
        for x in string.split(' '):
            if int(x, base=10).__divmod__(2)[1].__eq__(0):
                chet[0]+=1
            else:
                nechet[0]+=1
            c+=1
    else:
        return c
    return 0
# номер чётного номер нечётного, чёт\нечёт строка,
def nowel(string):
    count = 1
    chetnost = 0
    chet = 0
    nechet = 0
    for x in string.split(' '):
        if int(x, base=10).__divmod__(2)[1].__eq__(0):
            chetnost+=1
            chet=count
        else:
            chetnost-=1
            nechet=count
        count+=1
    if chetnost<0:
        return chet
    else:
        return nechet

        
print(nowel(test1))
print(nowel(test2))
print(nowel(test3))
print(nowel(test4))


def iq_test(n):
    n = [int(i)%2 for i in n.split()]
    if n.count(0)>1:
        return n.index(1)+1
    else:
        return n.index(0)+1
    
