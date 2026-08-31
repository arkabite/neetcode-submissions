# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur=head
        prev=None

        while cur:
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt

        reversed_head = prev
        if n==1:
            reversed_head = reversed_head.next
        else:
            track=1
            curhead=reversed_head
            while curhead and track<n-1:
                curhead=curhead.next
                track+=1
            
            if curhead and curhead.next:
                curhead.next=curhead.next.next
        
        prev = None
        cur = reversed_head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            
        return prev