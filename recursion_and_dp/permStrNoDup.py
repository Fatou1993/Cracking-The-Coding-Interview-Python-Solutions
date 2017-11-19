def permutationWithoutDup(s):
    """
    Compute all permutations of the string without duplicates
    :param s:
    :return:
    """

    def permutationWithoutDupHelper(index, results):
        if index == n :
            return results
        val = s[index]
        res = []
        if index == 0:
            res.append([s[0]])
        for l in results:
            for i in range(index+1):
                path = list(l)
                path.insert(i, val)
                res.append(path)
        return permutationWithoutDupHelper(index+1, res)
    n = len(s)
    res = permutationWithoutDupHelper(0,[])
    return ["".join(r) for r in res]

if __name__ == "__main__":
    s = "lov"
    res = permutationWithoutDup(s)
    print(len(res))
    for perm in res:
        print(perm)