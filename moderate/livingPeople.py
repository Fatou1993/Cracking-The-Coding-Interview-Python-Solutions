from collections import Counter

class Person(object):
    def __init__(self, b, d):
        self.birth = b
        self.death = d

def livingPeople(people):
    """

    Complexity O(n+m) where m = max diff years
    :param people:
    :return:
    """
    if not people :
        return None
    freq = [0]*101
    n = len(people)
    for person in people :
        birth, death = person.birth, person.death
        idxB = birth - 1900
        freq[idxB]+=1
        idxD = death - 1900
        if idxD+1 < n :
            freq[idxD+1] -= 1
    for i in range(1, 101):
        freq[i]+=freq[i-1]
    maxY, maxP = 1900, 0
    for i in range(101):
        if freq[i] > maxP :
            maxY = i + 1900
            maxP = freq[i]
    return maxY

if __name__ == "__main__":
    people = [Person(1900, 1990), Person(1987, 1995), Person(1990, 2000)]
    print(livingPeople(people))



