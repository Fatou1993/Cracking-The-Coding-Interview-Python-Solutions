from collections import namedtuple
def commonAncestor(root, u, v):
    Status = namedtuple("Status",('num_targets', "ancestor"))

    def lca_helper(root, u, v):
        if not root :
            return Status(0, None)
        left_result = lca_helper(root.left, u, v)
        if left_result.num_targets == 2 :
            return left_result
        right_result = lca_helper(root.right, u, v)
        if right_result.num_targets == 2 :
            return right_result
        num_nodes = left_result.num_targets + right_result.num_targets + (root in (u, v))
        return Status(num_nodes, root if num_nodes == 2 else None)

    return lca_helper(root, u, v).ancestor