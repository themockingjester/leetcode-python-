# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self,root):
        if root and self.validate:
            if root.left:
                if root.left.val == root.val:
                    self.validate = False
                    return 
                else:
                    self.check(root.left)
            self.lis.append(root.val)
            if root.right:
                if root.right.val == root.val:
                    self.validate = False
                    return
                else:
                    self.check(root.right)
            
    def isValidBST(self, root: TreeNode) -> bool:
        self.validate = True
        self.lis = []
        self.check(root)
        k = self.lis.copy()
        k = sorted(k)
        
        if self.validate==True:
            
            if k==self.lis:
                for i in range(len(self.lis)-1):
                    if self.lis[i]==self.lis[i+1]:
                        return False
                else:
                    return True
            else:
                return False
        else:
            return False
        
        
