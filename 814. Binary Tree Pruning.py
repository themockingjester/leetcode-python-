
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree(self,root):
        if root:
            if root.val==1:
                self.isonepresent = True
                return
            else:
                if root.left:
                    self.tree(root.left)
                if root.right:
                    self.tree(root.right)

    def check(self,root):
        self.isonepresent = False
        self.tree(root)
        if self.isonepresent==True:
            print("True")
            
            if root.left:
                self.check(root.left)
            if root.right:
                self.check(root.right)
        else:
            self.dic[root] = "True"
    def removing(self,root):
        
        if root.left:
            
            if root.left in self.dic:
                root.left = None
            else:
                self.removing(root.left)
        if root.right:
            if root.right in self.dic:
                root.right = None
            else:
                self.removing(root.right)
            
        
            

        
        
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if root==None:
            return root
        
        self.root = root
        self.dic = {}
        self.check(self.root)
        self.removing(self.root)
        print(self.dic)
        
        if self.root in self.dic:
            return None
        else:
            return self.root
     
    

    
    
    
    
    
#                                            Another Approach







class Solution:
    def check(self,root):
        if root:
            
            if root.left:
                root.left=self.check(root.left)
            if root.right:
                root.right=self.check(root.right)
            if root.left==None and root.right==None:
                if root.val==0:
                    return None
                else:
                    return root
            
            else:
                return root
    def pruneTree(self, root: TreeNode) -> TreeNode:
        
        root=self.check(root)
        return root
