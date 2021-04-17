# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self,root):
        if root:
            if self.val<root.val:
                if root.left==None:
                    k = TreeNode()
                    k.val = self.val
                    root.left = k
                    return
                else:
                    self.check(root.left)
            else:
                if root.right==None:
                    k = TreeNode()
                    k.val = self.val
                    root.right = k
                    return
                else:
                    self.check(root.right)
        
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        
        self.val = val
        if root==None:
            k = TreeNode()
            k.val = self.val
            root = k
        else:
            self.check(root)
           
            
        return root
            
