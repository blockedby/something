# Test.assert_equals(mix("Are they here", "yes, they are here"), "2:eeeee/2:yy/=:hh/=:rr")
from string import ascii_lowercase
# https://www.codewars.com/kata/5629db57620258aa9d000014/train/python
def mix(s1="mmmmm m nnnnn y&friend&Paul has heavy hats! &", s2="my frie n d Joh n has ma n y ma n y frie n ds n&"):
    # mix(s1, s2) --> "1:mmmmmm/=:nnnnnn/1:aaaa/1:hhh/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"
    # СНАЧАЛА ТЕ, У КОТОРЫЕ УНИКАЛЬНЫЕ
    def dic_in(string = "dddfff"):
        diction = dict()
        for letter in string:
            if letter in ascii_lowercase:
                if letter in diction.keys():
                    diction[letter]+=1
                else:
                    diction.update({letter:1})
        diction = {key:value for key,value in diction.items() if value!=1}
        dictionValues = dict()
        for value in diction.values():
            if value in dictionValues.keys():
                dictionValues[value]+=1
            else:
                dictionValues.update({value:1})
        return diction, dictionValues
    def to_one_list(dicNumber, v, dictionary):
        lL = {dicNumber:[]}
        for key,value in dictionary.items():
            if value == v:
                if dicNumber in lL.keys():
                    lL[dicNumber].append(key)
                    # КАКОЙ КИЙ ЭРРОР БЛЯТЬ
                else:
                   lL.update({dicNumber:[key]})
        return lL
    def bubble_abc(l = list()):
        if len(l) < 2:
            return l
        for first in l[0:-2]:
            for second in l[1:-1]:
                buffer = ""
                if second < first:
                    buffer = first
                    first = second
                    second = buffer
        return l
    def to_result(letter = 'a', count = 1):
        return ":" + letter * count
    def del_val(val,vNumb):
        nonlocal val1,val2
        if vNumb == 1:
            if val1[val]>1:
                val1[val]-=1
            else:
                val1.pop(val)
        elif vNumb == 2:
            if val2[val]>1:
                val2[val]-=1
            else:
                val2.pop(val)
        else:
            if val2[val]>1:
                val2[val]-=1
            else:
                val2.pop(val)
            if val1[val]>1:
                val1[val]-=1
            else:
                val1.pop(val)

    def to_garbage(dict1 = {}, dict2 = {}, key = "f"):
        nonlocal val1,val2
        if key in dict1.keys():
            
            if val1[dict1[key]]>1:
                val1[dict1[key]]-=1
            else:
                val1.pop(dict1[key])

            dict1.pop(key)
        if key in dict2.keys():
            
            if val2[dict2[key]]>1:
                val2[dict2[key]]-=1
            else:
                val2.pop(dict2[key])
            dict2.pop(key)
        return dict1,dict2
    def max_of_value(dictionary = {}, value = 1):
        for k,v in dictionary.items():
            if value==v:
                return k
    dic1,val1 = dic_in(s1)
    dic2,val2 = dic_in(s2)
    result = str()
    while dic1 and dic2:
        m1,m2 = max(val1.keys()) , max(val2.keys())
        if m1>m2:
            diKey = max_of_value(dic1,m1)
            result+="1"+to_result(diKey,m1) # max of letters in first
            dic1,dic2 = to_garbage(dic1,dic2,diKey)
        elif m2>m1: # m2>m1
            diKey = max_of_value(dic2,m2)
            result+="2"+to_result(diKey,m2)
            dic1,dic2 = to_garbage(dic1,dic2,diKey)  # max of letters in second
        elif m1==m2:  # 6
            # taking max count of letters in both dics and compare to lettersDict
            lettersDict = to_one_list(1,m1,dic1)
            lettersDict.update(to_one_list(2,m2,dic2))
            # to only one list
            lettersList = list()
            for value in lettersDict.values():
                for letter in value:
                    lettersList+=letter
            print("bubble")
            for first in lettersList[0:-2]:
                for second in lettersList[1:-1]:
                    buffer = ""
                    if second < first:
                        buffer = first
                        first = second
                        second = buffer
            # bubble-sorted lettersList
            print("Nu blia? {}".format(lettersList))
            # find parent string and add to result
            flag = False
            for elem in lettersList:
                if flag:
                    flag=False
                    break
                if lettersList.count(elem)==1:
                    # only one letter in list
                    if (elem,m1) in dic1.items():
                        result+="1"+to_result(elem[0],m1) # max of letters in first string
                        dic1,dic2 = to_garbage(dic1,dic2,elem[0])
                        # del_val(m1,1)
                    else:
                        # max of letters in second
                        result+="2"+to_result(elem[0],m2)
                        dic1,dic2 = to_garbage(dic1,dic2,elem[0])
                        # del_val(m2,2)
                else: # letter in two strings
                    result+="="+to_result(elem[0],m1)
                    dic1,dic2 = to_garbage(dic1,dic2,elem[0])
                    # del_val(m1,3)
                    flag = True
        
            # one of dictionaries is empty
    if dic1:
        # sort and make result
        pass
    else:
        # same thing like upper
        pass
    return result
# s[i:j:d] = t Срез от i до j (с шагом d) заменяется на (список) t

    
print(ascii_lowercase)
if "a"<"b": print("a")
mix()