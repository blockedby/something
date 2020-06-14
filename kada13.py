# Define a function that takes an integer argument and returns 
# logical value true or false depending on if the integer is a prime.

# Per Wikipedia, a prime number (or a prime) is a natural number 
# greater than 1 that has no positive divisors other than 1 and itself.

# Example
# is_prime(1)  /* false */
# is_prime(2)  /* true  */
# is_prime(-1) /* false */
# Assumptions
# You can assume you will be given an integer input.
# You can not assume that the integer will be only positive. 
# You may be given negative numbers as well (or 0).
# There are no fancy optimizations required, but still the most 
# trivial solutions might time out. Try to find a solution
# which does not loop all the way up to n.
def is_prime(num=100):
    if num <= 1 or num.__divmod__[1]==0:
        return False
    elif num == 2 or num == 3:
        return True
    else:
        for x in range(2,num):
            if x**2 < num:
                

print(is_prime(13))