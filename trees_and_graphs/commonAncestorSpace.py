def commonAncestor(root, u, v):
    def path(root, u):
        def helper_path(root, u, stack):
            if root == u:
                stack.append(u)
                return stack
            if not root:
                return None
            l = helper_path(root.left, u, stack + [root])
            if l:
                return l
            return helper_path(root.right, u, stack + [root])

        return helper_path(root, u, [])


    if not u or not v or not root:
        return None
    path_u = path(root, u)
    path_v = path(root, v)
    h_u, h_v = len(path_u), len(path_v)
    if h_u < h_v:
        path_u, path_v = path_v, path_u
    for i in range(1, min(h_u, h_v)):
        if path_u[i] != path_v[i]:
            return path_u[i - 1]
    return path_v[min(h_u, h_v) - 1]