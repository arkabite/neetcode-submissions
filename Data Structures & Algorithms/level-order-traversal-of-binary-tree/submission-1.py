# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        depth=0

        def bfs(node,depth):
            if node is None:
                return None

            if len(ans)==depth:
                ans.append([])
                
            ans[depth].append(node.val)
            depth+=1
            bfs(node.left,depth)
            bfs(node.right,depth)
        
        bfs(root,0)

        return ans