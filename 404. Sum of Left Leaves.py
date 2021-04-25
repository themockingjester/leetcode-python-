# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self,root,side):
        if root:
            if side == "left" and root.left == None and root.right == None:
                self.sum += root.val
            self.check(root.left,"left")
            self.check(root.right,"right")
            
    
            
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
        self.sum = 0
        self.check(root,None)
        
        
        return self.sum
