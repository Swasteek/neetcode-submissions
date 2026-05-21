class Solution:
    def __init__(self):
        self.k=0
        self.res=0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k=k
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            self.k-=1
            if self.k==0:
                self.res=node.val
                return 
            inorder(node.right)
        inorder(root)
        return self.res