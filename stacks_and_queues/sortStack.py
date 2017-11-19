def sortStack(stack):
    if not stack or len(stack) == 1 :
        return stack
    p = stack.pop()
    sm = []
    bg = []
    eq = [p]
    while stack :
        x = stack.pop()
        if x < p :
            sm.append(x)
        elif x == p :
            eq.append(x)
        else:
            bg.append(x)
    return sortStack(bg)+eq+sortStack(sm)

if __name__ == "__main__":
    stack = [1,2,3,4]
    print(stack)
    print(sortStack(stack))
    stack = [1,2,-1,-2,0,4,6,8,-10, 13,4,3,7,4,4,-20]
    print(stack)
    print(sortStack(stack))