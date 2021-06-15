import sys
from nose.tools import assert_equal, assert_true, assert_false
assert_equal(sys.version_info.major, 3)

# In old poor languages like Fortran and C, when you iterate, you have to 
# have a counter, increment it, and all that stuff.  Yeech. 
# Not so in Python.  You iterate over something that is iterable, that is, 
# that has (or can produce) a sequence of elements.  Like... a list! 
my_words = "I like to eat pizza with anchovies, I actually do!".split()
for w in my_words:
    print("My word is:", w)
    print("My word is:", w.capitalize())
    print("My word is:", w.upper())

#You can also iterate over pairs, consisting of the element index and the list element:
for i, w in enumerate(my_words):
    print("The word number", i, "is:", w)

# You can also use formatting options to specify the number of 
# digits to print for floating point numbers, etc. 
print("A gazillion is {:.2f}% less than a bazillion".format(15.67980))

def is_anagram(w1, w2):
    """Returns True iff word w1 is an anagram of word w2."""
    if w1 == "" and w2 == "":
        return True
    x1 = sorted(w1)
    x2 = sorted(w2)
    if x1 == x2:
        return True
    else:
        return False

    # YOUR CODE HERE
    raise NotImplementedError()
# 5 points. First, let's assume that the word does not contain repeated letters. 
print(is_anagram("home", "hemo"))
print(is_anagram("", ""))
print(is_anagram("figure", "refugi"))
print(is_anagram("seal", "coal"))

