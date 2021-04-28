# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self,root,lev):
        if root:
            if lev>self.maxdepth:
                self.bottom = root.val
                self.maxdepth=lev
            self.check(root.left,lev+1)
            self.check(root.right,lev+1)
    def findBottomLeftValue(self, root: TreeNode) -> int:
        self.maxdepth = 0
        self.bottom = None
        if root.left == None and root.right==None:
            return root.val
        self.check(root,0)
        return self.bottom
        
