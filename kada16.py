# https://www.codewars.com/kata/54a91a4883a7de5d7800009c/train/python

# МОЁ РЕЩЕНИЕ
# def increment_string(strng="foobar"):
#     if len(strng)==0:
#         return "1"
#     elif not strng[-1].isdigit():
#         return strng+"1"
#     else:
#         number = 0
#         num = list()
#         for f in strng[::-1]:
#             if f.isdigit():
#                 num.append(f)
#             else:
#                 break
#         for x in range(0,len(num)):
#             number+=int(num[x]) * (10**x)
#         numstr = str(number+1)
#     return strng[0:len(strng)-len(num)] + "0"*(len(num)-len(numstr)) + numstr

def increment_string(strng):
    
    # strip the decimals from the right
    stripped = strng.rstrip('1234567890')
    
    # get the part of strng that was stripped
    ints = strng[len(stripped):]
    
    if len(ints) == 0:
        return strng + '1'
    else:
        # find the length of ints
        length = len(ints)
    
        # add 1 to ints
        new_ints = 1 + int(ints)
    
        # pad new_ints with zeroes on the left
        new_ints = str(new_ints).zfill(length)
    
        return stripped + new_ints

print(increment_string("0foobar0099"))
