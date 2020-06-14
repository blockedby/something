# Test string for my 2 exercises
def to_jaden_case(string):
    words_list = string.split(' ')
    solution = ""
    for x in words_list:
        solution += (x.capitalize() + " ")
    solution = solution[:-1]
    return solution
test_string = "Test string for my 2 exercises"
print(to_jaden_case(test_string))