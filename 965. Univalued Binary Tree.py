# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self,root):
        if root:
            if root.val != self.fixval:
                self.fixval = False
                return
            else:
                if root.left:
                    self.check(root.left)
                if root.right:
                    self.check(root.right)
    def isUnivalTree(self, root: TreeNode) -> bool:
        if root:
            self.fixval = root.val
            if root.left:
                self.check(root.left)
            if root.right:
                self.check(root.right)
            print(self.fixval)  
            if isinstance(self.fixval,bool):
                
                return False
            else:
                return True
        else:
            return True
        
