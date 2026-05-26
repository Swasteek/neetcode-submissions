# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slowp,fastp=head,head
        for i in range(n):
            fastp=fastp.next
        if not fastp:
            return head.next
        while fastp.next:
            slowp,fastp=slowp.next,fastp.next
        ptr=slowp.next
        slowp.next=ptr.next
        del ptr
        return head