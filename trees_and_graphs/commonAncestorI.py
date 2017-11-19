def commonAncestor(u, v):
    """
    Returns lowest common ancestor
    :param u: node with parent
    :param v: node with parent
    :return: node
    """
    depth_u = depth(u)
    depth_v = depth(v)
    if depth_u < depth_v  :
        u, v = v, u
    for _ in range(abs(depth_u-depth_v)):
        u = u.parent
    while u is not v :
        u, v = u.parent, v.parent
    return u

def depth(u):
    res = 0
    while u :
        res += 1
        u = u.parent
    return res