# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(root):
            if not root:
                return 0
            lh=check(root.left)
            if lh==-1:
                return -1
            rh=check(root.right)
            if rh==-1:
                return -1
            if abs(lh-rh)>1:
                return -1
            return max(lh,rh)+1
        return check(root)!=-1


