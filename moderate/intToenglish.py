lookup = {
        0:"", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
        11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeenth",
        18: "eighteenth",
        19: "nineteen", 20: "twenty", 30: "thirty", 40: "fourty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty",
        90: "ninety", 100: "hundred",
        1000: "thousand"
    }

def getExpression(str) :

    exp = [int(str), ""]
    if exp[0] in lookup :
        exp[1] = lookup[exp[0]]
        return exp
    if exp[0] < 100 :
        exp[1] = lookup[(exp[0]/10)*10]
        if lookup[exp[0]%10] :
            exp[1] += " " + lookup[exp[0]%10]
    else:
        left = exp[0] % 100
        exp[1] = lookup[(exp[0] / 100)] + " hundred"
        if lookup[(left/10)*10]  :
            exp[1] += " and " + lookup[(left / 10) * 10]
        if lookup[left%10] :
            exp[1] += " " + lookup[left%10]
    return exp


def intToEnglish(n):
    """
    Given any integer, print an English phrase that describes it ( we willl consider only between 0 and 1M (not included)
    :param n:
    :return:
    """
    if n == 0 :
        return "zero"
    sign = 1
    if n < 0 :
        sign = -1
        n = -n
    s = list(str(n))
    num_digits = len(s)
    i = num_digits-1
    res = []
    seps = ["quadrillion", "billion", "million", "thousand"]
    j = 3
    while i >= 0 :
        lim = max(i - 2, 0)
        exp = getExpression("".join(s[lim: i+1]))
        if exp[1]:
            res.insert(0, exp[1])
        elif res[0] in seps:
            del res[0]
        if int(exp[0]) < 100 and int(exp[0]) > 0 and s[:lim]:
            res.insert(0, "and")
        if s[:lim]:
            res.insert(0, seps[j])
            j-=1
        i-=3
        print(res)
    res = "minus "+" ".join(res) if sign < 1 else " ".join(res)
    return res.strip()

if __name__ == "__main__":
    n = -1000010000023
    print(intToEnglish(n))



