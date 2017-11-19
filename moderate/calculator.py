MAPPING = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
}


class Solution(object):

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if not n :
            return 0
        stack = []
        num = 0
        sign = "+"
        for i in range(n):
            if s[i].isdigit():
                num = num*10+ord(s[i])-ord('0')
            if (not s[i].isdigit() and s[i] != " ") or i == n - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop()*num)
                elif sign == "/":
                    stack.append(stack.pop()/num)
                sign = s[i]
                num = 0
        res = 0
        while stack :
            res += stack.pop()
        return res


if __name__  == "__main__":
    input = "3+2*2"
    s = Solution()
    print(s.calculate(input))


