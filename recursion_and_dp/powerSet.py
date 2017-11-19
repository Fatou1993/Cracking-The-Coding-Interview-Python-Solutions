def powerSet(nums):
    """
    Generate all the subsets for a set
    :param nums:
    :return:
    """
    n = len(nums)
    size = 1 << n
    res = []
    for j in range(size):
        path = []
        for i in range(n):
            if j&(1<<i):
                path.append(nums[i])
        res.append(list(path))
    return res

if __name__ == "__main__":
    nums = [1,2,3,4]
    print(powerSet(nums))