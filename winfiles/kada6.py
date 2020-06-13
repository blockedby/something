# "()"              =>  true
# ")(()))"          =>  false
# "("               =>  false
# ( () ) 
# "( () )(( () () ) ())"  =>  true
# Test.assert_equals(valid_parentheses("  ("),False)
# Test.assert_equals(valid_parentheses(")test"),False)
# Test.assert_equals(valid_parentheses(""),True)
# Test.assert_equals(valid_parentheses("hi())("),False)
# Test.assert_equals(valid_parentheses("hi(hi)()"),True)


def valid_parentheses(string = "()"):
    if ("(" not in string)  or (")" not in string): # no paretheses in string
        return True
    # список скобок
    parList = [letter for letter in string if letter == "(" or letter == ")"]
    def lRecur(pList = list()):
        for parenth in pList:
            if parenth == "(":
                lRecur(pList)
            else:
                return True
        pass