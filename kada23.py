def anagrams(word = "abba", words=['aabb', 'abcd', 'bbaa', 'dada']):    # ans == ['aabb', 'bbaa']
    def dic_in(string = "dddfff"):
        diction = dict()
        for letter in string:
            if letter in diction.keys():
                diction[letter]+=1
            else:
                diction.update({letter:1})
        return diction
    wordDict = dic_in(word)
    anagramWords = [word for word in words if wordDict==dic_in(word)]
    return anagramWords
print(anagrams())