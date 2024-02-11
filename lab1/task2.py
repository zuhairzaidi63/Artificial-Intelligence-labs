# Question 2
numList = []      # Empty list

for i in range(0, 10):        # iterate loop 10 times to take 10 inputs
    numList.append(int(input("Enter a number : ")))       # take user integer input and insert it in list

for x in numList:         # iterate over list
    if x % 2 == 0:        # if completely divided by 2
        print("%d in this list is even " % x)   # then print it is even
    else:
        print("%d in this list is odd " % x)        # else it is odd



