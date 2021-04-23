# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            self.lis.append(root.val)
            self.inorder(root.right)
    def result(self,root):
        if root:
            self.result(root.left)
            root.val = self.lis[0]
            del self.lis[0]
            self.result(root.right)
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.lis = []
        self.inorder(root)
        self.lis = sorted(self.lis)
        self.result(root)
        
        
