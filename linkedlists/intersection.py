def length(head):
    res = 0
    curr = head
    while curr:
        res += 1
        curr = curr.next
    return res

def intersection(l1,l2):
    len1, len2 = length(l1), length(l2)
    if len1 < len2 :
        l1, l2 = l2, l1
    for _ in range(abs(len1-len2)):
        l1 = l1.next
    while l1 :
        if l1 == l2 :
            return l1
        l1 = l1.next
        l2 = l2.next
    return None
