# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        q=deque([root])
        s=""
        while q:
            node=q.popleft()
            if not node:
                s+="#,"
            else:
                s+=str(node.val)+","
                q.append(node.left)
                q.append(node.right)
        return s
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data=data.split(",")
        if data[0]=="#":
            return None
        x=data.pop(0)
        root=TreeNode(int(x))
        
        q=deque([root])
        while q:
            node=q.popleft()
            l=data.pop(0)
            if l!="#":
                left=TreeNode(int(l))
                node.left=left
                q.append(left)
            r=data.pop(0)
            if r!="#":
                right=TreeNode(int(r))
                node.right=right
                q.append(right)
        return root

