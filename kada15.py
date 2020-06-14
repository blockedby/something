# https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python
import string

def is_pangram(s = "Theeee quick, brown fox jumps over the lazy dog!" ):
    s = s.lower()
    letters = list()
    for f in s:
        if f in string.ascii_lowercase and not letters.count(f):
            letters.append(f)
    # letters(f for f in s if f in string.ascii_lowercase)
    return len(letters)==26
print(is_pangram())