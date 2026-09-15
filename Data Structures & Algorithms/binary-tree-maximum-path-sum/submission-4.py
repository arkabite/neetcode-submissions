# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPath=0
        self.res=float("-inf")

        def dfs(node):
            if node is None:
                return 0
            
            leftSum=max(dfs(node.left),0)
            rightSum=max(dfs(node.right),0)
            currSum=node.val+leftSum+rightSum
            self.res=max(self.res,currSum)

            return node.val+max(leftSum,rightSum)
        
        dfs(root)
        return self.res