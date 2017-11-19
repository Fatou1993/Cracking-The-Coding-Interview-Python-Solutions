def maxContiguousSum(arr):
    n = len(arr)
    maxSum, runningSum = float('-inf'), 0
    for i in range(n):
        runningSum+=arr[i]
        maxSum = max(maxSum, runningSum)
        if runningSum < 0 :
            runningSum = 0
    return maxSum

if __name__ == "__main__":
    arr = [-8,3,-2,4,-10]
    print(maxContiguousSum(arr))