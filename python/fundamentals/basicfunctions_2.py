# countdown

def countdown(x):
    x = int(input('Enter a number to countdown from: '));
    while(x > 0):
        print(x);
        x-=1;

countdown(5)

def countdown1(int):
    while(int > 0):
        print(int);
        int-=1;

countdown1(5)


#################
print("debug")
#print and return
def print_and_return(list):
    for i in list:
        print(list[i])
        return(list[i+1])
print_and_return([1,2,3,4,5,6])



#first plus length
def first_plus_length(list):
    first = 0
    last = 0
    print(list)
    for i in list:
        if(i == 1):
            first = i

    last = i
    #print(first)
    print(first+last)
first_plus_length([1,2,3,4,5])

#values greater than second
def greater_than_second(list):
    new_list = []
    for i in list:
        if(list[i] < list[2]):
            new_list.append(list[i])
    print(new_list)
greater_than_second([1,2,3,4,5])



def size_and_value(size, value):
    value_list = []
    for i in range(0, size):
        value_list.append(value)
    print(value_list)
size_and_value([4,3])