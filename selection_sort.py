#!/usr/local/bin/python3
# From Lucas Langer YouTube video: https://www.youtube.com/watch?v=JAvIvLMsLpU

'''
Pick out biggest element in list
put that in top of list
Find second biggest element in list
put that next in list
Repeat till done!
'''
import random

def createFile():
    f = open( "datafile.txt", "w" )
    for i in range( 1000 ):
        f.write(str(random.randrange( 1, 1000000000000 )) + "\n")

    f.close()

def swap_indices( myli, index1, index2 ):
    tmp = myli[index1]
    myli[index1] = myli[index2]
    myli[index2] = tmp

def selection_Sort(myList):
    for i in range( len(myList) ):
        biggest = i

        for j in range( i+1, len(myList) ):
            if myList[j] > myList[biggest]:
                biggest = j

        swap_indices( myList, biggest, i )

    return myList

createFile()
myNums = [int(num) for num in open("datafile.txt", "r").readlines()]
sorted_nums = selection_Sort(myNums)
print(sorted_nums)
