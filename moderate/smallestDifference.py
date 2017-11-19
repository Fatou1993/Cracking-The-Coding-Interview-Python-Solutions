def smallestDifference(a, b):
    n, m = len(a), len(b)
    for i in range(n):
        a[i] = (a[i], 1)
    for i in range(m):
        b[i] = (b[i], 2)
    while b :
        a.append(b.pop())
    a.sort(key=lambda x : x[0])
    diff = float("inf")
    vals = None
    i = 1
    for i in range(1,n+m):
        if a[i][1] != a[i-1][1]:
            if a[i][0]-a[i-1][0] < diff :
                diff = a[i][0]-a[i-1][0]
                vals = [(a[i-1][0], a[i-1][1]), (a[i][0], a[i][1])]
    return (diff, vals)

def closest(arr, x, size):
    left, right = 0, size - 1
    while left <= right :
        mid = (left+right)//2
        if arr[mid] == x :
            return mid
        elif arr[mid] < x :
            left = mid+1
        else:
            right = mid-1
    if left == size :
        left -= 1
    return arr[left] if (right < 0 or abs(arr[left]-x) < abs(arr[right]-x)) else arr[right]


def smallestDifferenceWithoutExtraSpace(a, b):
    """
    Time Complexity (O(nlogn + mlogm))
    Space Complexity O(1)
    :param a:
    :param b:
    :return:
    """
    n, m = len(a), len(b)
    a.sort()
    b.sort()
    idx1, idx2 = 0, 0
    diff = float('inf')
    while idx1 < n and idx2 < m :
        if abs(a[idx1]-b[idx2]) < diff :
            diff = abs(a[idx1]-b[idx2])
        if a[idx1] < b[idx2] :
            idx1 += 1
        else:
            idx2 += 1
    return diff


if __name__ == "__main__":
    a = [1,15,11,2]
    b = [4,12,19,23,127,235]
    print(smallestDifferenceWithoutExtraSpace(a, b))
