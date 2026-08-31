# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]

        def check(node,depth):
            if node is None:
                return None

            if len(ans)==depth:
                ans.append([])
            
            ans[depth].append(node.val)
            check(node.left,depth+1)
            check(node.right,depth+1)

        check(root,0)
        return ans