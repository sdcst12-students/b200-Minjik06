#!python3


def getIntegers(myList):
    # myList : expected list or tuple
    # iterate through myList and add all the integers to the new list
    integers = []
    for i in range(len(myList)):
        if myList[i]-int(myList[i])==0:
            integers.append(myList[i])

    return integers

def getFactor(myList,number):
    # myList : expected list or tuple
    # number : integer
    # iterate through the list and add the number to the list if
    # it is a factor of the number
    factors = []
    for i in range(len(myList)):
        if number/myList[i]==0:
            factors.append(myList[i])

    return factors

def getNegatives(myList):
    # myList : expected list or tuple
    # iterate through myList and add all the negative numbers to the new list
    negatives = []
    for i in range(len(myList)):
        if myList[i]<0:
            negatives.append(myList[i])
    return negatives

def getIntersection(list1,list2):
    # list 1: expected list or tuple
    # list 2: expected list or tuple
    # return a sorted list of numbers that is in both lists
    # the intersection of the 2 number sets
    common = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i]==list2[j]:
                common.append(list1[i])

    return common

def getUnion(list1,list2):
    # list 1: expected list or tuple
    # list 2: expected list or tuple
    # return a sorted list of numbers that is in either of the lists
    # duplicate values will be ignored
    union = []
    for i in range(len(list1)):
        union.append(list1[i])
    for j in range(len(list2)):
        union.append(list1[j])
    union=union.sort()
    for k in range(len(union-1)):
        if union[k]==union[k+1]:
            del union[k+1]

    return union   

def getMerge(list1,list2):
    # list 1: expected list or tuple
    # list 2: expected list or tuple
    # add the elements of list2 into list1
    # if the list2 element is in list1, add it at the position where it occurs in list1
    # if the list2 element is not in list1, add it to the end
    i=0
    j=0
    while i < len(list1):
        while j < len(list2):
            if list1[i]==list2[j]:
                list1.insert(i+1,list1[i])
                list2.pop(j)
            j+=1
        i+=1
                
    return list1


def main():
    easy1 = [5,10,15,2,4,6,8]
    easy2 = [-2,-4,-6,2,4,6,0.1]
    numbers1 = [3,5,8,12,11,19,10,7,2,15,25,34,16,32,50,60,100,-3,0.25]
    numbers2 = [3,7,11,15,19,23,27,31,35,39,44,50]
    try:
        assert getIntegers([3,4,1.2,1.3,5]) == [3,4,5]
        assert getFactor(range(10),12) == [1,2,3,4,6]
        assert getNegatives([-3,-1,0,1,4]) == [-3,-1]
        assert getUnion(easy1,easy2) == [-6, -4, -2, 0.1, 2, 4, 5, 6, 8, 10, 15]
        assert getIntersection(easy1,easy2) == [2,4,6]
        assert getMerge(easy1,easy2) == [5,10,15,2,2,4,4,6,6,8,-2,-4,-6,0.1]
        print("All assertions passed")
    except:
        print("At least 1 assertion failed")

if __name__ == "__main__":
    main()
