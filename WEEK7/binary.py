# 199. Binary Tree Right Side View
class Solution9:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        BFS (Level-order traversal) - take rightmost node at each level
        Time: O(n)
        Space: O(w) where w is max width
        """
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            
            for i in range(level_size):
                node = queue.popleft()
                
                # Add rightmost node of this level
                if i == level_size - 1:
                    result.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return result
    
    def rightSideView_dfs(self, root: Optional[TreeNode]) -> List[int]:
        """
        DFS approach - visit right child first
        Time: O(n)
        Space: O(h)
        """
        result = []
        
        def dfs(node, level):
            if not node:
                return
            
            # First time visiting this level
            if level == len(result):
                result.append(node.val)
            
            # Visit right first, then left
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)
        
        dfs(root, 0)
        return result