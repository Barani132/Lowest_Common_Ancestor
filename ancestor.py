#Lowest Common Ancestor (BST)
def lca(root, p, q):
    if p < root.val and q < root.val:
        return lca(root.left, p, q)
    if p > root.val and q > root.val:
        return lca(root.right, p, q)
    return root.val
