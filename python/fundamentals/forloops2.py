# Biggie Size
def biggie_size(list):
    new_list = []
    for i in list:
        #print(i)
        #print(list)
        if i < 0:
            new_list.append(i)
        else:
            new_list.append("big")
    print(new_list)
biggie_size([-1, 3, 5, -5])

# count positives
def count_positives(list):

    x = abs(list[-1])
    list.pop()
    list.append(x)
    return list
print(count_positives([1,1,1,1,-1]))

# average
def average(list):
    return sum(list) / len(list)
print(average([1,2,3,4]))


# length
def list_length(list):
    return len(list)
print(list_length([1,2,3,4,5,6]))

# min
def list_min(list):
    return min(list)
print(list_min([1,2,3,4,5]))


def list_max(list):
    return max(list)
print(list_max([1,2,3,4,5]))


