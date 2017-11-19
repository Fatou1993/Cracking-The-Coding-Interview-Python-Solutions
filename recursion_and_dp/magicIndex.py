def magicIndex(A):
    """
    Finds index i such that A[i] = i with an array of distinct integers
    :param A: array of integers
    :return:
    """
    n = len(A)
    left, right= 0, n-1
    while left <= right :
        mid = (left+right)//2
        if A[mid] == mid :
            return mid
        elif A[mid] < mid :
            left = mid + 1
        else :
            right = mid-1
    return None

def magicIndexWithDuplicates(arr):
    """
    Key idea if A[5] == 3 A[4] wont work for example
    if A[5] = 9 A[6][7], ..A[8] wont work
    :param arr:
    :return:
    """
    def binarySearch(arr, low, high):
        if low > high :
            return -1
        mid = (low+high)//2
        if arr[mid] == mid :
            return mid
        midVal = arr[mid]
        leftIndex = min(mid-1, midVal)
        left = binarySearch(arr,low,leftIndex)
        if left != - 1:
            return left
        rightIndex = max(mid+1,midVal)
        right = binarySearch(arr,rightIndex, high)
        return right

    return binarySearch(arr, 0, len(arr)-1)


if __name__ == "__main__":
    arr = [-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13]
    print(magicIndexWithDuplicates(arr))
    arr = [-10, -1, 3, 3, 10, 30, 30, 50, 100]
    print(magicIndexWithDuplicates(arr))



