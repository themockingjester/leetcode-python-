# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self,root,value):
        if root:
            
            if root.left == None and root.right==None:
                if value == True:
                    self.lis1.append(root.val)
                else:
                    self.lis2.append(root.val)
                
            else:
                if root.left:
                    self.check(root.left,value)
                if root.right:
                    self.check(root.right,value)
               
        
            
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        self.lis1 = []
        self.lis2=[]
        if root1:
            self.check(root1,True)
        if root2:
            self.check(root2,False)
            
        if self.lis1 == self.lis2:
            return True
        else:
            return False
