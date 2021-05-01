# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self,root):
        if root:
            if root.left:
                if root.left.val==self.target and root.left.left==None and root.left.right==None:
                    root.left = None
                    self.performed = True
                else:
                    self.check(root.left)
            if root.right:
                if root.right.val==self.target and root.right.left==None and root.right.right==None:
                    root.right = None
                    self.performed = True
                else:
                    self.check(root.right)
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        self.target = target
        self.performed = True
        while self.performed:
            self.performed = False
            if root:
                if root.val == self.target and root.left == None and root.right==None:
                    root = None
                else:
                    self.check(root)

        return root
