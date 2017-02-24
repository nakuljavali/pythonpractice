import sortLib as sl

def mergesort(inputList):
    if len(inputList) == 1:
        return inputList

    # Floor Division
    mid = len(inputList)//2
    list1 = mergesort(inputList[:mid])
    list2 = mergesort(inputList[mid:])
    return merge(list1, list2)

def merge(list1, list2):
    retList = []
    while (len(list1) > 0 and len(list2) > 0):
        if (list1[0] > list2[0]):
            retList.append(list2[0])
            list2.pop(0)
        else:
            retList.append(list1[0])
            list1.pop(0)

    if list1:
        retList.extend(list1)
    if list2:
        retList.extend(list2)

    return retList


if __name__ == '__main__':
    ipList = sl.inputListCli()
    outList = mergesort(ipList)
    print outList
