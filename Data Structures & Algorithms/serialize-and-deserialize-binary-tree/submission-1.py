# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res=[]
        def dfs(node):
            if node is None:
                res.append("N")
                return None
            
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        val= ",".join(res)
        return val
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data=data.split(",")
        self.i=0
        def buildTree():
            if data[self.i]=="N":
                self.i+=1
                return None
            root=TreeNode(int(data[self.i]))
            self.i+=1
            root.left=buildTree()
            root.right=buildTree()
            return root
        return buildTree()

