# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        cur=head
        first,second=head,head
        while second and second.next:
            first=first.next
            second=second.next.next
        
        second=first.next
        prev=first.next=None

        while second:
            nxt=second.next
            second.next=prev
            prev=second
            second=nxt
        
        first=head
        second=prev

        while second:
            tmp1=first.next
            tmp2=second.next
            first.next=second
            second.next=tmp1
            second=tmp2
            first=tmp1
            
