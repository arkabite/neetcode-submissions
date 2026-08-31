# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res=float("-inf")

        def dfs(node):
            if node is None:
                return 0
            
            leftPath=max(dfs(node.left),0)
            rightPath=max(dfs(node.right),0)

            currSum=node.val+leftPath+rightPath

            self.res=max(self.res,currSum)

            return  node.val+ max(leftPath,rightPath)
        
        dfs(root)
        return self.res