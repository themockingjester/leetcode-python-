# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self,root,level):
        if root:
            if self.maxlevel<level:
                self.maxlevel = level
            self.check(root.left,level+1)
            self.check(root.right,level+1)

    def maxDepth(self, root: TreeNode) -> int:
        self.maxlevel=0
        self.check(root,1)
        return self.maxlevel
        
