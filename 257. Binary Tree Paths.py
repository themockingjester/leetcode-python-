# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self,root,s):
        if root:
            if root.left==None and root.right==None:
                k = str(root.val)
                s=s+k
                self.lis.append(s)
                return
            if root.left:
                self.check(root.left,s+str(root.val)+"->")
            if root.right:
                self.check(root.right,s+str(root.val)+"->")
         
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root:
            self.lis = []
            if root.left==None and root.right == None:
                self.lis.append(str(root.val))
                
            else:
                if root.left:
                    s = str(root.val)+"->"
                    self.check(root.left,s)
                if root.right:
                    s = str(root.val)+"->"
                    self.check(root.right,s)
        return self.lis
