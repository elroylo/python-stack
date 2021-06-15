s = 'A string'
t = "It's nice to be able to choose the delimiters"
l = t.split()
print(l)
for i in l:
    print(i)
i.capitalize()
for i in l:
    print(i)

set1 = {'cat', 'dog'}
set2 = {'bird', 'mouse', 'cat'}
set3 = {'dog', 'cat'}
print(set1 | set2) # union
print(set1 & set2) # intersection
print(set1 - set2) # difference
# We can add elements to a set... 
set1.add('duck')
print(set1)
set1.add('dog')
print(set1)
# ... and as you can see, sets really have no repeated elements,
# so if you add a dog to a set containing already a dog, 
# nothing changes.

# A quick way to remove duplicates from a list is to turn it 
# into a set, then back into the list.  This loses the ordering though,
# as sets do not preserve the order of the elements of the lists
# from which they were created:
l = ['a', 'b', 'c', 'g', 'c', 'd', 'f', 'g']
l_uniq = list(set(l))
l_uniq

# If you want to preserve the ordering, then you can use iteration
# (covered later) and do as follows:
l_uniq = [] # list
occurrences = set() # set
for s in l:
    if s not in occurrences:
        l_uniq.append(s) # list append
        occurrences.add(s) # set add
l_uniq
