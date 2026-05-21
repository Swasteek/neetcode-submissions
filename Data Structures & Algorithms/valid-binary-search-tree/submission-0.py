class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(node, low, up):
            if not node:
                return True
            
            if not (low < node.val < up):
                return False
            
            return check(node.left, low, node.val) and check(node.right, node.val, up)
        
        return check(root, float('-inf'), float('inf'))