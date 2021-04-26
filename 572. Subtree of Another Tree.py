# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def nodes(self,root,level,side):
        if root and self.isSubtreevar==False:
            
            self.ctr+=1
            self.lis.append(str(root.val)+str(level)+str(side))
            self.nodes(root.left,level+1,"left")
            self.nodes(root.right,level+1,"right")
    
        
            
    def check(self,root): 
        if root and self.isSubtreevar==False:
            self.ctr = 0
            self.lis = []
            self.nodes(root,0,None)
            
            if self.lis==self.treeitems and self.ctr == self.totalnodesintreeT:
                self.isSubtreevar = True
                
            self.check(root.left)
            self.check(root.right)
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        self.t = t
        self.isSubtreevar = False
        self.lis = []
        self.ctr=0
        self.nodes(t,0,None)
        self.totalnodesintreeT = self.ctr
        self.treeitems = self.lis.copy()
        
        
        self.check(s)
        
        return self.isSubtreevar
