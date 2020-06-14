# Return the number (count) of vowels in the given string.

# We will consider a, e, i, o, and u as vowels for this Kata.

# The input string will only consist of lower case letters and/or spaces.

# def getCount(s):
#     return sum(c in 'aeiou' for c in s)
teststr="fffffdddddaaaaa"
testlist = ['1', 2 , 3 , 4 , 5]
testset = {'a' , 'i' , 'e' , 'o' , 'u'}
def getCount(inputStr):
    num_vowels = 0
    num_vowels_list = ['a' , 'i' , 'e' , 'o' , 'u']
    for x in inputStr:
        if num_vowels_list.__contains__(x):
            num_vowels += 1
    return num_vowels
print(getCount("ddyhjknigygoojju"))