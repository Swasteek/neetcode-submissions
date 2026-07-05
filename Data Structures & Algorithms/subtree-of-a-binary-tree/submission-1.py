# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val!=q.val:
                return False
            return check(p.left,q.left) and check(p.right,q.right)
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        q=deque([root])
        ans=False
        while q:
            node=q.popleft()
            if node.val==subRoot.val:
                ans=ans or check(node,subRoot)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return ans
            