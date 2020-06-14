# Given the triangle of consecutive odd numbers:

#              1                1
#           3     5             2
#        7     9    11          3
#    13    15    17    19       4
# 21    23    25    27    29    5
# 11                      15    sum = 1+2+3+4+5 = ap(n)=15
# 5 stolb => 15 slogaemih => sum(5 poslednih)
# ...
# Calculate the row sums of this triangle from the row index (starting at index 1) e.g.:

# row_sum_odd_numbers(1); # 1
# row_sum_odd_numbers(2); # 3 + 5 = 8
def row_sum_odd_numbers(n):
    summ = 0
    for x in range(sum(range(1,n+1))-n+1, sum(range(1,n+1))+1):
        summ+=1 + (x - 1)*2
    return summ


# >>> mapped = map(abs, [-1, -2, -3])
# >>> list(mapped)
# [1, 2, 3]
# map(ap(), range(ap(n)-n+1, ap(n)))
def ap(n):
        return 1 + (n - 1)*2
print(row_sum_odd_numbers(1))
print(row_sum_odd_numbers(2))
print(row_sum_odd_numbers(3))
print(row_sum_odd_numbers(4))
print(row_sum_odd_numbers(13)) #2197