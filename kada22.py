def decipher_this(string = "72olle 103doo 100ya"):
#     #your code here
# ("65 119esi 111dl 111lw 108dvei 105n 97n 111ka"), "A wise old owl lived in an oak")
# ("84eh 109ero 104e 115wa 116eh 108sse 104e 115eokp"), "The more he saw the less he spoke")
# ("84eh 108sse 104e 115eokp 116eh 109ero 104e 104dare"), "The less he spoke the more he heard")
# ("87yh 99na 119e 110to 97ll 98e 108eki 116tah 119esi 111dl 98dri"), "Why can we not all be like that wise old bird")
# ("84kanh 121uo 80roti 102ro 97ll 121ruo 104ple"), "Thank you Piotr for all your help")
    sList = string.split()
    result = ""
    for word in sList:
        # for letter in word:
        a = [num for num in word if num.isdigit()]
        l = len(a)-1
        num = 0
        for elem in a:
            num += int(elem)*(10**l)
            l -= 1
        first = chr(num)
        letters = [letter for letter in word if not letter.isdigit()]
        if len(letters)==0:
            result += first
        elif len(letters)==1:
            result += first+letters[0]
        else:
            result += first+letters[-1]
            for letter in letters[1:-1]:
                result+=letter
            result += letters[0]
        result+=" "
    return result[0:-1]

print(decipher_this())