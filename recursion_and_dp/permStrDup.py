def getPerms(s):
    result = []
    n = len(s)
    seen = set()
    getPermsHelper("",s,n,result, seen)
    return result

def getPermsHelper(prefix, remainder, remaining_length, result, seen):
    if remaining_length == 0:
        if prefix not in seen:
            result.append(prefix)
            seen.add(prefix)
    for i in range(remaining_length):
        before = remainder[:i]
        c = remainder[i]
        after = remainder[(i+1):]
        getPermsHelper(prefix+c,before+after,remaining_length-1,result, seen)
    return

if __name__ == "__main__":
    s = "lovo"
    res = getPerms(s)
    print(len(res))
    for perm in res:
        print(perm)