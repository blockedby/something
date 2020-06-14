# This time no story, no theory. The examples below show you how to write function accum:

# Examples:

# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"
# The parameter of accum is a string which includes only letters from a..z and A..Z.
def accum(s):
    result = ""
    counter = 0
    for x in s:
        counter+=1
        for z in range(1,counter+1):
            result+=x
        result+=" "
    result = result.title()
    return result.replace(" ","-")[0:-1]
print(accum("RqaEzty"))

def accum(s):
    i = 0
    result = ''
    for letter in s:
        result += letter.upper() + letter.lower() * i + '-'
        i += 1
    return result[:len(result)-1]