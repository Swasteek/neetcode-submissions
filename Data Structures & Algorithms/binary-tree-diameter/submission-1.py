# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxi=[0]
        def height(root):
            if not root:
                return 0
            lc,rc=height(root.left),height(root.right)
            maxi[0]=max(maxi[0],lc+rc)
            return max(lc,rc)+1
        height(root)
        return maxi[0]