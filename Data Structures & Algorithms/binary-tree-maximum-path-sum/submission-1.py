# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.maxi=float('-inf')
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def check(root):
            if not root:
                return 0
            lsum=max(0,check(root.left))
            rsum=max(0,check(root.right))
            self.maxi=max(self.maxi,lsum+rsum+root.val)
            return max(lsum,rsum)+root.val
        check(root)
        return self.maxi