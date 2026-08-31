# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(node, low=float('-inf'), high=float('inf')):
                    # An empty tree is a valid BST
                    if not node:
                        return True
                    
                    # The current node's value must be strictly within the low and high bounds
                    if not (low < node.val < high):
                        return False
                    
                    # 1. When going left, the node's value becomes the new upper bound (high)
                    # 2. When going right, the node's value becomes the new lower bound (low)
                    # Both subtrees must be valid (hence the 'and')
                    return check(node.left, low, node.val) and check(node.right, node.val, high)
                
        return check(root)
        