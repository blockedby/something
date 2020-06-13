# https://www.codewars.com/kata/5420fc9bb5b2c7fd57000004/train/python
def highest_rank(arr = [12, 10, 8, 12, 7, 6, 4, 10, 12]):
    myDict = {a:0 for a in arr} # dictionary comprehension
    # for key in myDict.keys():
    #     if key in arr:
    #         arr.remove(key)
    #         myDict[key] += 1
    for elem in arr:
        myDict[elem] +=1
    maxValue = max(myDict.values())
    maxKey = 0
    for item in myDict.items():
        if item[1] == maxValue and item[0] > maxKey:
            maxKey=item[0]
    return maxKey
print(highest_rank())