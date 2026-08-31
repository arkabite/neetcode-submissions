# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def isValidBST(node,left=float("-inf"),right=float("inf")):
            if node is None:
                return True
            
            if node.val>left and node.val<right:
                return isValidBST(node.left,left,node.val) and isValidBST(node.right,node.val,right)
            else:
                return False
            
        return isValidBST(root)
