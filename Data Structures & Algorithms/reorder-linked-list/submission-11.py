# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow,fast=head,head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        second=slow.next
        prev=slow.next=None
        while second:
            nxt=second.next
            second.next=prev
            prev=second
            second=nxt
        
        first=head
        second=prev

        while second:
            n1=first.next
            n2=second.next
            first.next=second
            second.next=n1
            first=n1
            second=n2