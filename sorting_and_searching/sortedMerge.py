def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """
    idx1, idx2, curr = m - 1, n - 1, m + n - 1
    while idx2 >= 0:
        if idx1 >= 0 and nums1[idx1] > nums2[idx2]:
            nums1[curr] = nums1[idx1]
            idx1 -= 1
        else:
            nums1[curr] = nums2[idx2]
            idx2 -= 1
        curr -= 1

if __name__ == "__main__":
    nums1 = [2, 4, 5, 0, 0]
    print(nums1)
    m = 3
    nums2 = [1, 3]
    n = 2
    merge(nums1,m,nums2,n)
    print(nums1)