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
        s=[]
        while q:
            node=q.popleft()
            if node:
                s.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                s.append("#")
            
        return ",".join(s)


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nums=data.split(',')
        
        if nums[0]=='#':
            return None

        root=TreeNode(int(nums[0]))
        i=1
        q=deque([root])
        while q:
            node=q.popleft()
            if nums[i]!="#":
                node.left=TreeNode(int(nums[i]))
                q.append(node.left)
            i+=1
            if nums[i]!="#":
                node.right=TreeNode(int(nums[i]))
                q.append(node.right)
            i+=1
        return root
                

