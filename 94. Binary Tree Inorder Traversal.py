# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self,root):
        if root:
            self.check(root.left)
            self.lis.append(root.val)
            
            self.check(root.right)
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.lis=[]
        self.check(root)
        return self.lis
