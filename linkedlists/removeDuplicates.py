from ListNode import ListNode
import collections

def removeDuplicates(head):
    if not head or not head.next:
        return head
    dup = getDuplicates(head)
    if not dup :
        return head
    dummyHead = ListNode(0)
    dummyHead.next = head
    curr = dummyHead
    while curr.next :
        if curr.next.val in dup :
            curr.next = curr.next.next
        else:
            curr = curr.next
    return dummyHead.next


def getDuplicates(head):
    """
    Returns duplicates in a linkedlist
    :param head: ListNode
    :return: list of duplicated elements
    """
    freq = collections.defaultdict(int)
    curr = head
    while curr :
        freq[curr.val]+=1
        curr = curr.next
    return [k for k in freq if freq[k] > 1]