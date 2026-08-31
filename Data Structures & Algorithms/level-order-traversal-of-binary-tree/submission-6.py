# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res=[]

        def buildTraversal(node,depth):
            if node is None:
                return None

            if len(res)==depth:
                res.append([])

            res[depth].append(node.val)
            depth+=1
            buildTraversal(node.left,depth)
            buildTraversal(node.right,depth) 

        buildTraversal(root,0)

        return res           
