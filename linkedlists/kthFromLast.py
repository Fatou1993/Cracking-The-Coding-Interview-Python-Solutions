
def kthFromLast(head, k):
    """
    Print value of kth element from last convention = 1th = last element
    :param head: LinkedList
    :param k: int
    :return: LinkedList
    """

    if not head:
        return head
    p1 = p2 = head
    for _ in range(k):
        if not p2 :
            print('Element not accessible')
            return None
        p2 = p2.next
    while p2:
        p2 = p2.next
        p1 = p1.next
    return p1 if p1 else None




