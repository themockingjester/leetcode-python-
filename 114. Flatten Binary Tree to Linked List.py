# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self,root):
        if root:
            self.lis.append(root.val)
            self.check(root.left)
            self.check(root.right)
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.lis = []
        k = root
        self.check(root)
        for i in range(len(self.lis)):
            if root:
                if root.left:
                    root.left = None
                root.val = self.lis[i]
                if root.right==None and i<len(self.lis)-1:
                    root.right= TreeNode()
                root=root.right
        return k

        
        
