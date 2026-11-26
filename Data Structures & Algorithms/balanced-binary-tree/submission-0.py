# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        left=self.maxDepth(root.left)
        right=self.maxDepth(root.right)
        val=abs(left-right)

        if val>1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)

    def maxDepth(self,root):
        if root is None:
            return 0
        
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1