def binarySearch(listy, left, right, target):
    while left <= right :
        mid = (left+right)//2
        midVal = listy.elementAt(mid)
        if  midVal == target :
            return mid
        elif midVal > target :
            right = mid - 1
        else:
            left = mid + 1
    return -1

def sortedSearchNoSize(listy, target):
    """

    :param listy:
    :return:
    """
    idx = 1
    while listy.elementAt(idx) != - 1 and listy.elementAt(idx) < x :
        idx*=2
    return binarySearch(listy, idx/2, idx, target)