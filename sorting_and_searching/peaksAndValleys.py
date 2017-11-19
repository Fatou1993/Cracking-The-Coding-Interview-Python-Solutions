def sortPeaksValleys(arr):
    n = len(arr)
    if n <= 1 :
        return arr
    if arr[0] < arr[1]:
        arr[0], arr[1] = arr[1], arr[0]
    isValley = True
    for i in range(2,n):
        if (isValley and arr[i] < arr[i-1]) or (not isValley and arr[i] > arr[i-1]):
            arr[i], arr[i-1] = arr[i-1], arr[i]
        isValley = not isValley
    return arr

if __name__ == "__main__":
    arr = [9,1,0,4,8,7]
    print(sortPeaksValleys(arr))