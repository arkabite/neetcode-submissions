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

        first=slow.next
        prev=slow.next=None
        while first:
            nxt=first.next
            first.next=prev
            prev=first
            first=nxt
        
        first=prev
        second=head

        while first:
            temp1=first.next
            temp2=second.next
            second.next=first
            first.next=temp2
            second=temp2
            first=temp1
        
        

