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
        def check(node):
            if not node:
                return 0
            lsum=max(0,check(node.left))
            rsum=max(0,check(node.right))
            self.maxi = max(self.maxi, lsum + rsum + node.val)

            return max(lsum,rsum)+node.val
        check(root)
        return self.maxi