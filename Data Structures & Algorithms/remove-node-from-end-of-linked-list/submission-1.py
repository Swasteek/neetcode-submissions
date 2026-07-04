# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fp=head
        for i in range(n):
            fp=fp.next
        slow=head
        if not fp:
            return head.next
        while fp and fp.next:
            slow=slow.next
            fp=fp.next
        slow.next=slow.next.next
        return head
