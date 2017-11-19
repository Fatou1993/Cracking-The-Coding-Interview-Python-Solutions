from ListNode import ListNode
def reverseList(head):
    if not head:
        return head
    prev, curr, nex = None, head, None
    while curr:
        nex = curr.next
        curr.next = prev
        prev = curr
        curr = nex
    return prev

def isPalindrome(head):
    if not head or not head.next:
        return True
    dummyHead = ListNode(0)
    dummyHead.next = head
    p1 = p2 = dummyHead
    while p2 and p2.next:
        p2 = p2.next.next
        p1 = p1.next
    sP = p1.next
    p1.next = None
    fP = dummyHead.next
    sP = reverseList(sP)
    while sP :
        if sP.val != fP.val:
            return False
        sP = sP.next
        fP = fP.next
    return True
