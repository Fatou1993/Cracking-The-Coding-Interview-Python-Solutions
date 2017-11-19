def hanoiTowers(N):
    currStack, newStack, helperStack = list(reversed(range(N))), [], []
    print("currSack:", currStack, "newStack:", newStack, "helperStack:",helperStack)
    hanoiTowersHelper(N, currStack, newStack, helperStack)
    print("currSack:", currStack, "newStack:", newStack, "helperStack:", helperStack)
    return newStack

def hanoiTowersHelper(N, currStack, newStack, helperStack):
    if N == 0 :
        return
    hanoiTowersHelper(N-1, currStack, helperStack, newStack)
    newStack.append(currStack.pop())
    hanoiTowersHelper(N-1,helperStack,newStack,currStack)

if __name__ == "__main__":
    n = 8
    res = hanoiTowers(n)



