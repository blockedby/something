# Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.
# Hint: This is just to test your memory of the basic arithmetic commands, work backwards from 100.25
# import math
# result1 = ((100.25*100.25) ** (1/2) + math.frexp(8)[1]*0)
# print(f'(100.25*100.25) ** (1/2) + math.frexp(8)*0 = {result1}')
# Answer these 3 questions without typing code. Then type code to check your answer.
# What is the value of the expression 4 * (6 + 5) = 44

# What is the value of the expression 4 * 6 + 5 = 29

# What is the value of the expression 4 + 6 * 5 = 34

# What is the type of the result of the expression 3 + 1.5 + 4? float

# What would you use to find a number’s square root, as well as its square?

# In [ ]:
# # Square root:
# In [ ]: if >0 **1/2
# # Square: **2

# Strings
# Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:

# In [ ]: 
# s = 'hello'
# s[1] or s[-4]
# # Print out 'e' using indexing
# Reverse the string 'hello' using slicing:

# In [ ]:
# s ='hello'
# s = s[::-1]
# # Reverse the string using slicing
# Given the string hello, give two methods of producing the letter 'o' using indexing.

# In [ ]:
# s ='hello'
# # Print out the 'o'

# # Method 1:   already done
# In [ ]:
# # Method 2:


# Lists
# Build this list [0,0,0] two separate ways.

# In [ ]:
# # Method 1:
mylist = [0,0,0]
# In [ ]:
mylist = [0]
mylist = mylist + mylist + mylist
# # Method 2:
# Reassign 'hello' in this nested list to say 'goodbye' instead:

# In [ ]:
list3 = [1,2,[3,4,'hello']]
list3[2][2]='goodbye'
# Sort the list below:

# In [ ]:
list4 = [5,3,4,6,1]
list4.sort()
# Dictionaries
# Using keys and indexing, grab the 'hello' from the following dictionaries:

# In [ ]:
d = {'simple_key':'hello'}
print(d['simple_key'])
# # Grab 'hello'
# In [ ]:
d = {'k1':{'k2':'hello'}}
print(f"{d['k1']['k2']}")
# # Grab 'hello'
# In [ ]:
# # Getting a little tricker
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
mystr = d['k1'][0]['nest_key'][1][0]
print(mystr)
# print(f"{d['k1']['nest_key'][1]}")
# #Grab hello
# In [ ]:
# # This will be hard and annoying!
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
mystr = d['k1'][2]['k2'][1]['tough'][2][0]
print(mystr)
# Can you sort a dictionary? Why or why not?


# Tuples
# What is the major difference between tuples and lists?

#its static

# How do you create a tuple?

mytuple = (1,2,5,7,8.0)

# Sets
# What is unique about a set?

#unsorted, unique, no duplicates

# Use a set to find the unique values of the list below:

# In [ ]:
list5 = [1,2,2,33,4,4,11,22,3,3,2]
set5 = set()
set5.update(list5)
set5(list5)
print(set5)
if (3.0)==(3):
    print("DA")