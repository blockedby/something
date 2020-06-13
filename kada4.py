def encrypt_this(text="The more he saw the less he spoke"):
    wordText = list()
    result = ""
    if text == "":
        return result
    for word in text.split(' '):
        if len(word)==2:
            result+=(str(ord(word[0])) + word[1])
        elif len(word)==1:
            result+=(str(ord(word)))
        else:
            result+=( str(ord(word[0])) + word[-1] + word[2:-1] + word[1] )
        result+=' '
    return result[0:-1]
# print("Thank"[1:-1])
# ord(obj) returns unicode 
print(encrypt_this())
print("84eh 109ero 104e 115wa 116eh 108sse 104e 115eokp")
# https://www.codewars.com/kata/5848565e273af816fb000449/train/python