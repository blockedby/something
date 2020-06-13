def josephus_survivor(initSeq = 7, number = 3):
    sequence = [i for i in range(1 , initSeq+1)]
    last = 0 # индекс последнего
    while len(sequence)>1:
        currNumber = number
        while currNumber>len(sequence):
            currNumber = currNumber - len(sequence)
            # уменьшаем прыжок на длину очереди,
            # если прыжок больше длины.
        # тут у на есть последний удалённый элемент,
        # нужно посчитать индекс следующего удалённого элемента
        # индекс первого по счёту = индекс следующего,
        # поэтому удалить нужно (currnumber - 1 + last) < (длина)
        #   [0:6] elem        3       -1
        #   [0:6] elem        1       -1
        if len(sequence) > (currNumber+last):
            last = currNumber - 1 + last # 2 0
            sequence.pop(last)
        elif len(sequence) <(currNumber+last):
            last = currNumber + last - len(sequence) - 1
            sequence.pop(last)
        else: # delete last elem in seq
            sequence.pop(currNumber-1+last)
            last = 0
    return sequence[0]

print(josephus_survivor(14,2))
# [1,2,3,4,5,6,7] - initial sequence 3
# [1,2,4,5,6,7] => 3 is counted out                               4+3 = 7       
# [1,2,4,5,7] => 6 is counted out        last = 4        [1,2,4,5,7]
# [1,4,5,7] => 2 is counted out                             !
# [1,2,3,4,5,6,7] - initial sequence 7 7 7 7 7 
# [1,2,3,4,5,6]
# [2,3,4,5,6]

# [1,2,3,4,5,6,7] - initial sequence
# [1,2,4,5,6,7] => 3 is counted out
# [1,2,4,5,7] => 6 is counted out
# [1,4,5,7] => 2 is counted out
# [1,4,5] => 7 is counted out
# [1,4] => 5 is counted out
# [4] => 1 counted 