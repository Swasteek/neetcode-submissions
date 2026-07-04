# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast=head,head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        h2=slow.next
        slow.next=None

        #Reverse
        temp=h2
        prev=None
        while temp:
            ptr=temp.next
            temp.next=prev
            prev=temp
            temp=ptr
        
        h1,h2=head,prev
        while h1 and h2:
            x=h2.next
            h2.next=h1.next
            h1.next=h2
            h1=h1.next.next
            h2=x




        