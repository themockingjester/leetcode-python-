# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self,root,level):
        if root:
            if root.left==None and root.right == None:
                self.lis.append(level)
                
                
            self.check(root.left,level+1)
            self.check(root.right,level+1)
    def minDepth(self, root: TreeNode) -> int:
        self.minlevel = 0
        self.lis = []
        if root:
            self.check(root,1)
        else:
            return 0
        return min(self.lis)
