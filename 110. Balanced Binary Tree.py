# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def heightfinder(self,root,level):
        if root and self.answer==True:
            if level>self.maxheight:
                self.maxheight = level
            
            self.heightfinder(root.left,level+1)
            self.heightfinder(root.right,level+1)
        else:
            return self.maxheight
            
    def traversal(self,root):
        if root and self.answer == True:
            leftheight = 0
            rightheight = 0
            self.maxheight = 0
            self.heightfinder(root.left,1)
            leftheight = self.maxheight
            self.maxheight = 0
            self.heightfinder(root.right,1)
            rightheight = self.maxheight
            if abs(leftheight-rightheight)>1:
                self.answer=False
            else:
                self.traversal(root.left)
                self.traversal(root.right)
    def isBalanced(self, root: TreeNode) -> bool:
        self.maxheight = 0
        self.answer = True
        self.traversal(root)
        
        print(self.maxheight)
        return self.answer
    
        
            
                
        
