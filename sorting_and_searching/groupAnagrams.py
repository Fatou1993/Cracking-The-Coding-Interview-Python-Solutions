def groupAnagrams(arr):
    """
    Sort an array of strings such that all anagrams are next to each other
    O(nlogn) time complexity
    O(n) space complexity
    :param arr:
    :return:
    """
    arr.sort()
    tmp = list(arr)
    n = len(arr)
    for i in range(n):
        tmp[i] = [sorted(tmp[i]),i]
    tmp.sort(key=lambda x: x[0])
    for i in range(n):
        tmp[i][0] = arr[tmp[i][1]]
    for i in range(n):
        arr[i] = tmp[i][0]

if __name__ == "__main__":
    arr = ["oze", 'silent', "cat", "rat", "tar", "listen", "tac", "act", "zoe"]
    print(arr)
    groupAnagrams(arr)
    print(arr)
