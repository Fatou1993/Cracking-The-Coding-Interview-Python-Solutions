def subSort(nums):
    """

    :param nums:
    :return:
    """
    size = len(nums)
    if size <= 1 : return None #array already sorted
    startE = float('inf')
    n = 0
    prevE = nums[0]
    for i in range(1,size):
        if nums[i] < prevE :
            startE = min(startE, nums[i])
            n = i
        else:
            prevE = nums[i]
    if startE == float('inf'): #array already sorted
        return None
    m = 0
    while m < size and nums[m] <= startE :
        m+=1
    return (m, n)
if __name__ == "__main__":
    nums = [1,2,4,7,10,11,7,12,6,7,16,18,19]
    print(subSort(nums))


