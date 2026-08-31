# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPathSum=float("-inf")

        def search(node):
            if node is None:
                return 0
                
            leftMax=max(search(node.left),0)
            rightMax=max(search(node.right),0)

            val=node.val+leftMax+rightMax

            self.maxPathSum=max(self.maxPathSum,val)

            return node.val+max(leftMax,rightMax)
        
        search(root)
        return self.maxPathSum