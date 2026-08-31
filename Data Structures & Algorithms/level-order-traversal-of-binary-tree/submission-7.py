# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res=[]

        def buildTree(node,depth):
            if node is None:
                return None
            
            if depth==len(res):
                res.append([])
            
            res[depth].append(node.val)
            depth+=1
            buildTree(node.left,depth)
            buildTree(node.right,depth)
        
        buildTree(root,0)
        return res
