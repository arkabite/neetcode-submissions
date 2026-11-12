# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        str1=""
        cur=l1

        while cur:
            str1+=str(cur.val)
            cur=cur.next
        
        str2=""
        cur=l2
        while cur:
            str2+=str(cur.val)
            cur=cur.next
        
        str1=str1[::-1]
        str2=str2[::-1]

        res=str(int(str1)+int(str2))
        res=res[::-1]
        n=len(res)
        print(res,str1,str2)

        dummy=ListNode()
        tail=dummy
        i=0
        while i<n:
            val=int(res[i])
            tail.val=val
            if (i+1)<n:
                tail.next=ListNode(int(res[i+1]))
            else:
                tail.next=None
                
            tail=tail.next
            i+=1
        
        return dummy

            
        