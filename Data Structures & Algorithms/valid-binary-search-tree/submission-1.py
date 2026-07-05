# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(low,node,up):
            if not node:
                return True
            if not (low<node.val<up):
                return False
            return check(low,node.left,node.val) and check(node.val,node.right,up)
        return check(float('-inf'),root,float('inf'))