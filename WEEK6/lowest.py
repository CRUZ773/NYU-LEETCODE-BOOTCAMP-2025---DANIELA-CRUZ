# 236. Lowest Common Ancestor of a Binary Tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution3:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Recursive approach: If current node is p or q, or p and q are in different subtrees
        Time: O(n)
        Space: O(h) where h is height
        """
        # Base case: if root is None or root is one of p or q
        if not root or root == p or root == q:
            return root
        
        # Search in left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If both left and right are not None, root is LCA
        if left and right:
            return root
        
        # Otherwise, return whichever is not None
        return left if left else right
