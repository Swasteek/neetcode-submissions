# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        vd=defaultdict(int)
        q=deque([(root,0)])

        while q:
            node,y=q.popleft()
            vd[y]=node.val
            if node.left:
                q.append((node.left,y+1))
            if node.right:
                q.append((node.right,y+1))
        return [vd[y] for y in sorted(vd.keys())]

        