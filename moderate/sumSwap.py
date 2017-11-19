def search(arr, size, target):
    left, right = 0, size - 1
    while left <= right :
        mid = (left+right)//2
        if arr[mid] == target :
            return mid
        elif arr[mid] < target :
            left = mid + 1
        else:
            right = mid - 1
    return None

def sumSwap(arr1, arr2):
    m, n = len(arr1), len(arr2)
    swap = False
    if m > n : #arr1 is the smallest array
        swap = True
        arr1, arr2 = arr2, arr1
        m, n = n, m
    sum1, sum2 = sum(arr1), sum(arr2)
    if (sum1 - sum2)%2 : return None
    arr1.sort()
    for j in range(n):
        target = (sum1 - sum2)//2 + arr2[j]
        idx = search(arr1, m, target) #search i
        if idx is not None :
            tmp = arr2[j]
            arr2[j] = arr1[idx]
            arr1[idx] = tmp
            print(sum(arr1), sum(arr2))
            return (arr2[j], arr1[idx]) if not swap else (arr1[idx], arr2[j])
    return None

if __name__ == "__main__":
    arr1 = [4,1,2,1,1,2]
    arr2 = [3,6,3,3]
    print(arr1, arr2)
    print(sum(arr1), sum(arr2))
    print(sumSwap(arr1, arr2))

