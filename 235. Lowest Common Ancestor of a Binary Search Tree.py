# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def check(self,root,lis):
        if root and self.ctr<2:
            lis.append(root)
            if root==self.p:
                self.dic[root]=lis
                self.ctr+=1
            if root == self.q:
                self.dic[root]=lis
                self.ctr+=1
            self.check(root.left,lis.copy())
            self.check(root.right,lis.copy())
           
                
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.dic = {}
        self.ctr=0
        self.p = p
        self.q = q
        self.check(root,[])
        k = self.dic[p]
        l = self.dic[q]
        lis2 = []
        if len(k)<=len(l):
            for i in k:
                if i in l:
                    lis2.append(i)
        else:
            for i in l:
                if i in k:
                    lis2.append(i)
        return lis2[-1]
            
            
            
        
