def partition(self, head, x):
    """
    Partition a linkedlist such taht el < x appear before
    O(n) time complexity 0(1) space complexity"
    :type head: ListNode
    :type x: int
    :rtype: ListNode
    """

    if not head:
        return head
    dummyHead = ListNode(0)
    dummyHead.next = head
    prev = dummyHead
    curr = head
    small = dummyHead
    while curr:
        if curr.val < x:
            tmp = curr.val
            # suppress the node
            prev.next = curr.next
            curr = prev.next
            # put the node at right place and remove duplicate
            node = ListNode(tmp)
            node.next = small.next
            small.next = node
            small = small.next
            # put prev at right place
            while prev.next != curr:
                prev = prev.next
        else:
            prev = curr
            curr = curr.next
    return dummyHead.next