import sys
print("Your version of Pyton is: {major}.{minor}".format(
    major=sys.version_info.major, minor=sys.version_info.minor))
assert sys.version_info.major >= 3 and sys.version_info.minor >= 6, "You are running an old version"

def pair_swap(l):
    """Swaps the elements of l in pairwise fashion.  If the list is of
    odd length, the last element is left in place."""
    # YOUR CODE HERE
    if len(l) < 2:
        return l
    for index in range(0,len(l) - 1,2):
        l[index], l[index + 1] = l[index + 1], l[index]
    return l

assert pair_swap([]) == []
assert pair_swap([1, 2, 3, 4]) == [2, 1, 4, 3]
assert pair_swap(['a']) == ['a']
assert pair_swap([1, 2, 3, 4, 5]) == [2, 1, 4, 3, 5]



def compress(l): 
    i = 0
    new_list = []
    if len(l) == 0:
        return l
    while( i < len(l) - 1) :   
        # Counting occurrences of s[i] 
        count = 0  
        while l[i] == l[i + 1] :   
            i = i + 1
            count = count + 1              
            if i + 1 == len(l): 
                break          
        #print(str(count) + str(l[i]),end = "")
        #new_list.extend((count, l[i]))
        new_list.append((count, l[i]))
        i = i + 1
    return new_list

print(compress([]))
print(compress(['a']))
print(compress(['a', 'a']))  
print(compress([1, 2, 2, 3, 3, 3, 0, 'cat']) == [(1, 1), (2, 2), (3, 3), (1, 0), (1, 'cat')])

assert compress([]) == []
assert compress(['a']) == [(1, 'a')]
assert compress(['a', 'a']) == [(2, 'a')]        