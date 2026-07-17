# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        mpp=defaultdict(int)
        q=deque([root])
        if not root:
            return []
        lv=0
        while q:
            n=len(q)
            for i in range(n):
                node=q.popleft()
                mpp[lv]=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            lv+=1
        res=[]
        print(mpp.items())
        for i in range(lv):
            res.append(mpp[i])
        return res