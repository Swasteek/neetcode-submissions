# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def findkth(node,k):
            temp=node
            cnt=1
            while temp and cnt<k:
                temp=temp.next
                cnt+=1
            return temp
        def reverse(head):
            if not head or not head.next:
                return head
            prev=head
            temp=head.next
            head.next=None
            while temp:
                ptr=temp.next
                temp.next=prev
                prev=temp
                temp=ptr
            return prev
        
        
        if not head or k == 1:
            return head
        dummy=ListNode(-1)
        prevNode=dummy
        temp=head
        while temp:
            kthnode=findkth(temp,k)
            if not kthnode:
                prevNode.next=temp
                break
            nxt=kthnode.next
            kthnode.next = None
            kthnode=reverse(temp)
            prevNode.next=kthnode
            temp.next=nxt
            prevNode=temp
            temp=nxt
        return dummy.next
            

        