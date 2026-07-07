"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        q=deque([node])
        mpp={}
        while q:
            curr=q.popleft()
            newCurr=Node(curr.val)
            mpp[curr]=newCurr
            for nei in curr.neighbors:
                if nei not in mpp:
                    q.append(nei)
        
        for nide in mpp:
            for nei in nide.neighbors:
                mpp[nide].neighbors.append(mpp[nei])
        return mpp[node]