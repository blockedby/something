# https://www.codewars.com/kata/514b92a657cdc65150000006/train/python

def solution(number=10):
    # numbers from 3 to @number@
    # for f in range(3,number+1):
    #     if f%15==0:
    answer = sum([f for f in range(1,number) if f%15==0 or f%3==0 or f%5==0])
    return answer
print(solution())