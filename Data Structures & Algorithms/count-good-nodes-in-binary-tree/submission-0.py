# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.res=0
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root,cmax):
            if root.val >= cmax:
                self.res+=1
                cmax=root.val
            if root.left:
                dfs(root.left,cmax)
            if root.right:
                dfs(root.right,cmax)
        dfs(root,float('-inf'))
        return self.res