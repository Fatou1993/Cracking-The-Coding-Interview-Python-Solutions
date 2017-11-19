def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    n = len(nums)
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[left] == target:
            return left
        elif nums[mid] < target:
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                if nums[left] < target:
                    right = mid - 1
                else:
                    left = mid + 1
        else:
            if nums[mid] >= nums[left]:
                if nums[left] > target:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                right = mid - 1
    return -1

if __name__ == "__main__":
    arr = [15,16,19,20,25,1,3,4,5,7,10,14]
    target = 5
    res = search(arr, target)
    print(res)