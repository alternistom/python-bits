biggerList = [1,2,3,4,5,6,7,8,9,10]
smallerList = [1,2,9,10]

s = set(smallerList)
listOfDifferences = [x for x in biggerList if x not in s]

# listOfDifferences will be [3,4,5,6,7,8]