# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        mh=[]
        cnt=0
        for i in lists:
            heapq.heappush(mh,(i.val,cnt,i))
            cnt+=1
        dummy=ListNode(-1)
        temp=dummy
        while mh:
            val,b,node=heapq.heappop(mh)
            temp.next=node
            node=node.next
            if node:
                heapq.heappush(mh,(node.val,cnt+1,node))
                cnt+=1
            temp=temp.next
        return dummy.next
        