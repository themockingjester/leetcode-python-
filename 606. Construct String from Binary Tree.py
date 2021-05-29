# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self,root):
        if root:
            self.str+='('
            self.str+=str(root.val)
            if root.left==None and root.right:
                self.str+='()'
                self.check(root.right)
            elif root.right==None and root.left:
                self.check(root.left)
                
            else:
                self.check(root.left)
                self.check(root.right)
            self.str+=')'
        
            
    def tree2str(self, t: TreeNode) -> str:
        self.str=''
        if t:
            self.str+=str(t.val)
            if t.left==None and t.right:
                self.str+='()'
                self.check(t.right)
            elif t.right==None and t.left:
                self.check(t.left)
                
            else:
                self.check(t.left)
                self.check(t.right)
            
        return self.str
