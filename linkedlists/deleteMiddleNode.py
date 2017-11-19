def deleteMiddleNode(node):
    """

    :param node: Node
    :return: bool
    """
    if not node or not node.next :
        return False
    node.val = node.next.val
    node.next = node.next.next
    return True