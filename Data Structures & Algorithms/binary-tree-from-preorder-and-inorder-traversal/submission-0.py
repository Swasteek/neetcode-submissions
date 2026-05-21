# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def f(preorder,preStart,preEnd,inorder,inStart,inEnd,inMP):
            if preStart>preEnd:
                return None
            root=TreeNode(preorder[preStart])
            ind=inMp[root.val]
            numsleft=ind-inStart
            root.left=f(preorder,preStart+1,preStart+numsleft,inorder,inStart,ind-1,inMP)
            root.right=f(preorder,preStart+numsleft+1,preEnd,inorder,ind+1,inEnd,inMP)
            return root






        inMp={val:i for i,val in enumerate(inorder)}
        root=f(preorder,0,len(preorder)-1,inorder,0,len(inorder)-1,inMp)
        return root