import random
def randInt(min, max):
    #min = int(input("Enter the min: "))
    #max = int(input("Enter the max: "))
    if min == "":
        min = 0
    if max == "":
        max = 0
    return random.randint(min, max)
print(randInt(min,max)) 		    # should print a random integer between 0 to 100
#print(randInt(0,50)) 	    # should print a random integer between 0 to 50
#print(randInt(50,100)) 	    # should print a random integer between 50 to 100
#print(randInt(50,500))    # should print a random integer between 50 and 500
