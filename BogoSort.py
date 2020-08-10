#TODO remove this comment
import random
from matplotlib import pyplot as plt
import time

#takes in array to sort
def bogoSort(ar):
    Sorted = False
    attempts = 0

    while not Sorted:
        attempts += 1
        #shuffles array
        random.shuffle(ar)
        for i in range(len(ar)-1):
            #if any number is out of order at all then we shuffle again
            if ar[i]>ar[i+1]:
                Sorted = False
                break
            else:
                Sorted = True
    return attempts

#holds avg number of iteration
list_of_results = []

#this for loop runs from 2-10, dictating the size of the to-be-sorted array
for i in range(2,10):
    list_of_times = []
    for j in range(50):
        #holds number of iterations per run (runs 50 times)

        #this is the list that will be randomly generated
        list = []
        unique_numlist = []

        for k in range(1,i+1):
            unique_numlist.append(k)

        list_generated = False
        while not list_generated:
            randomNumber = random.randint(0, len(unique_numlist)-1)
            list.append(unique_numlist.pop(randomNumber))

            if(len(unique_numlist)==0):
                list_generated = True

        attempt_count = 0
        #bogoSort returns the number of iterations it took to successfully sort
        attempt_count = bogoSort(list)
        list_of_times.append(attempt_count)
    #averages the num of its and adds it to the list of avg number of its
    list_of_results.append(sum(list_of_times)/50)

log_list = []
for i in range(0,8):
    log_list.append(10**i)

print("It took",time.process_time(),"seconds to run this code.")
xbar = [2,3,4,5,6,7,8,9]
ybar = list_of_results
print(ybar)
plt.plot(xbar,ybar,'b-')
plt.yscale("log")
plt.xlabel("Size of the sorted list")
plt.ylabel("Number of iterations required ")
plt.xticks(xbar)
plt.yticks(log_list)
plt.grid()
plt.show()






