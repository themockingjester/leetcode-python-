# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self,root,s):
        if root:
            if root.left == None and root.right==None:
                s+=str(chr(root.val+97))
                self.lis.append(s[::-1])
            else:
                s+=str(chr(root.val+97))
                self.check(root.left,s)
                self.check(root.right,s)
    def smallestFromLeaf(self, root: TreeNode) -> str:
        s = ""
        self.lis = []
        
        self.check(root,s)
        k = sorted(self.lis)
        
        return k[0]
            
        
