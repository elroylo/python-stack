# Write a function ziplist that, given two lists, produces a list of pairs, with the first element of the pair coming from the first list, and the second from the second list.  
# The output list of pairs must be as long as the longest of the input lists, and the missing elements from the shorter input list give rise to None in the output list. 

from nose.tools import assert_equal, assert_true, assert_false
import sys
assert_equal(sys.version_info.major, 3)

def ziplist(list1, list2):
    list3 = []
    #if len(list1) == 0 and len(list2) == 0:
    #    list3.append(,)
    #    return list3
    if len(list1) > len(list2):
        print(">")
        for i in range(len(list1)):
            try:
                list3.append((list1[i], list2[i]))
            except:
                list3.append((list1[i], None))
        return list3

    elif len(list1) == len(list2):
        print("==")
        for i in range(len(list1)):
            list3.append((list1[i], list2[i]))
        return list3
            

    elif len(list1) < len(list2):
        print("<")
        for i in range(len(list2)):
            try:
                list3.append((list1[i], list2[i]))
            except:
                list3.append((None, list2[i]))
        return list3


print(ziplist(['a', 'b', 'c'], [1, 2,3]))
print(ziplist([], []))
print(ziplist([1, 2], []))
print(ziplist([1], ['a', 'b']))

assert_equal(ziplist(['a', 'b', 'c'], [1, 2, 3]), [('a', 1), ('b', 2), ('c', 3)])
assert_equal(ziplist([], []), [])
assert_equal(ziplist([1, 2], []), [(1, None), (2, None)])
assert_equal(ziplist([1], ['a', 'b']), [(1, 'a'), (None, 'b')])


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

def closest_neighbor(point_list):
    # YOUR CODE HERE
    point_list.sort()
    if len(point_list) < 2:
        return None
    return (point_list[-2], point_list[-1])

print(closest_neighbor([(1, 2), (4, 5), (5, 5), (4, 1)]))
print((closest_neighbor([(1, 2)]), None))
#assert_equal(closest_neighbor([(1, 2), (4, 5), (5, 5), (4, 1)]), ((4, 5), (5, 5)))
#assert_equal(closest_neighbor([(1, 2)]), None)


from collections import Counter 
def threeormore(l):
    c = Counter(l)
    if l == []:
        print(set())
        return set()

    for i in range(len(l)):
        if c[i] > 2:
            print (l[i])


threeormore([1, 3, 5, 4, 3, 7, 6, 3, 7, 7, 7, 1, 2, 0, 3, 1])
threeormore([])

def olympic_average(els):
    if len(els) == 0:
        return None
    x = sum(els) / len(els)
    print (x)
    y = x % 1
    x = x - y
    if y < 0.25:
        return x
    elif y > 0.24 and y < 0.74:
        y = 0.5
        x += y
        return x
    elif y > 0.74:
        y = 1
        x += y
        return x

assert_equal(olympic_average([5, 3, 4, 5]), 4.5)
assert_equal(olympic_average([5, 6, 3, 4, 10]), 5)


#assert_equal(threeormore([1, 3, 5, 4, 3, 7, 6, 3, 7, 7, 7, 1, 2, 0, 3, 1]), {1, 3, 7})
assert_equal(threeormore([]), set())

class MyQueue(): 
    
    def __init__(self):
        # YOUR CODE HERE
        self.q1 = []
        self.q2 = []

        
    def enqueue(self, x):
        # YOUR CODE HERE
        while len(self.q1) != 0:  
            self.q2.append(self.q1[-1])  
            self.q1.pop()

            self.q1.append(x)  
  
        # Push everything back to q1  
        while len(self.q2) != 0:  
            self.q1.append(self.q2[-1])  
            self.q2.pop()


    def dequeue(self):
        # YOUR CODE HERE
        if len(self.q1) == 0:  
            print("Queue is currently empty")
        x = self.q1[-1]  
        self.q1.pop()  
        return x 

q = MyQueue()
q.enqueue('banana')
q.enqueue('apple')
assert_equal(q.dequeue(), 'banana')
q.enqueue('cherry')
assert_equal(q.dequeue(), 'apple')
assert_equal(q.dequeue(), 'cherry')
assert_equal(q.dequeue(), None)

