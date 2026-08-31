"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        old_To_New={}
        cur=head
        while cur:
            old_To_New[cur]=Node(cur.val)
            cur=cur.next
        
        cur=head
        while cur:
            old_To_New[cur].next=old_To_New.get(cur.next)
            old_To_New[cur].random=old_To_New.get(cur.random)
            cur=cur.next
        
        return old_To_New[head]