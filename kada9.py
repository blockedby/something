# Take 2 strings s1 and s2 including only letters from a to z.
#  Return a new sorted string, the longest possible, containing distinct letters,

# each taken only once - coming from s1 or s2.
# Examples:
# a = "xyaabbbccccdefww"
# b = "xxxxyyyyabklmopq"
# longest(a, b) -> "abcdefklmopqwxy"

# a = "abcdefghijklmnopqrstuvwxyz"
# longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"

a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
c = set()
for x in (a+b):
    c.add(x)
c = sorted(c)
a =''.join(str(s) for s in c)

# def longest(a1, a2):
#     return "".join(sorted(set(a1 + a2)))