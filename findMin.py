__author__ = 'Karen Clark'

import time
from random import randrange

'''
From InteractivePython.org
Self Check

Write two Python functions to find the minimum number in a list.
The first function should compare each number to every other number on the list. O(n2)O(n2).
The second function should be linear O(n)O(n).

Why is this O(n2)? Look at the number of for loops. There are two, so this is O(n2).
We can validate this by running find_min() with a list of random numbers, and timing
the results.
'''

# O(n2) implementation
def findMin(alist):
    overallmin = alist[0]
    for i in alist:
        issmallest = True
        for j in alist:
            if i > j:
                issmallest = False
        if issmallest:
            overallmin = i
    return overallmin


# O(n) implementation
def findMin(alist):
    minsofar = alist[0]
    for i in alist:
        if i < minsofar:
            minsofar = i
    return minsofar

print(findMin([5, 4, 2, 1, 0]))
print(findMin([0, 5, 4, 2, 1]))

for listSize in range(1000,10001,1000):
    alist = [randrange(100000) for x in range(listSize)]
    start = time.time()
    print(findMin(alist))
    end = time.time()
    print("size: %d time: %f" % (listSize, end - start))