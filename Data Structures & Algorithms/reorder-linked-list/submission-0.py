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
        
        dummy,n1,n2=ListNode(-1),head,prev
        temp=dummy
        pehla=True
        while temp:
            if pehla:
                temp.next=n1
                n1=n1.next if n1 else None
            else:
                temp.next=n2
                n2=n2.next if n2 else None
            temp=temp.next
            pehla=not pehla
        


        