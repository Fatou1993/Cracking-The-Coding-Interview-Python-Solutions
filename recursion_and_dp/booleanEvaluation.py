def countEval(s, val):
    def strToBoolean(s):
        return s == "1"

    def countEvalHelper(s, val, memo):
        if not s :
            return 0
        if len(s) == 1 :
            return strToBoolean(s) == val
        #place to put the paren
        if str(val) + s in memo :
            return memo[str(val) + s]
        ways = 0
        n = len(s)
        for i in range(1,n,2):
            left = s[:i]
            right = s[(i+1):]
            leftTrue = countEvalHelper(left, True, memo)
            leftFalse = countEvalHelper(left, False,memo)
            rightTrue = countEvalHelper(right, True, memo)
            rightFalse = countEvalHelper(right, False, memo)
            total = (leftTrue+leftFalse)*(rightFalse+rightTrue) #number of ways to express s
            totalTrue = 0
            if s[i] == "^":
                totalTrue+= leftTrue*rightFalse + leftFalse*rightTrue
            elif s[i] == "&":
                totalTrue+=leftTrue*rightTrue
            else:
                totalTrue+=leftTrue*rightTrue + leftFalse*rightTrue + leftTrue*rightFalse
            subways = totalTrue if val else total - totalTrue
            ways+=subways
        memo[str(val) + s] = ways
        return ways

    memo = {}
    res = countEvalHelper(s, val, memo)
    #print(memo)
    return res

if __name__ == "__main__":
    print(countEval("0&0&0&1^1|0", True))
