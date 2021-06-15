def is_anagram(w1, w2):
    """Returns True iff word w1 is an anagram of word w2."""
    if w1 == "" and w2 == "":
        return True
    x1 = sorted(w1.lower())
    x2 = sorted(w2.lower())
    if x1 == x2:
        return True
    else:
        return False
    raise NotImplementedError()

print(is_anagram("home", "hemo"))
print(is_anagram("", ""))
print(is_anagram("figure", "refugi"))
print(is_anagram("seal", "coal"))

input1StrA = "yes"
input1StrB = "eys"
#Output: true
print(is_anagram(input1StrA, input1StrB))

input2StrA = "yes"
input2StrB = "eYs"
#Output: true
print(is_anagram(input2StrA, input2StrB))
input3StrA = "no"
input3StrB = "noo"
#Output: false
is_anagram(input3StrA, input3StrB)
input4StrA = "silent"
input4StrB = "listen"
#Output: true
is_anagram(input4StrA, input4StrB)
