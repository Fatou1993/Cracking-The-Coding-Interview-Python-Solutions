from collections import Counter
def numCommonElements(g, s):
    if not g or not s :
        return 0
    cg = Counter(g)
    cs = Counter(s)
    num_psuedo_hits = 0
    for key in cg :
        if key in cs :
            num_psuedo_hits += min(cg[key], cs[key])
    return num_psuedo_hits

def masterMind(guess, solution):
    n = len(guess)
    if n != len(solution): return None
    g, s = [], []
    num_hits = 0
    for i in range(n):
        if guess[i] == solution[i]:
            num_hits+=1
        else:
            g.append(guess[i])
            s.append(solution[i])
    return (num_hits, numCommonElements(g, s))

if __name__ == "__main__":
    guess = "GGRR"
    solution = "RGBR"
    print(masterMind(guess, solution))
