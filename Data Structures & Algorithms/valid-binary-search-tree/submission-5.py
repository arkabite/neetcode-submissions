# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validBST(node,left=float("-inf"),right=float("inf")):
            if node is None:
                return True
            
            if node.val>left and node.val<right:
                return validBST(node.left,left,node.val) and validBST(node.right,node.val,right)
            else:
                return False
        
        return validBST(root)
