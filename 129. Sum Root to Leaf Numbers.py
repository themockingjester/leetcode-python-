# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self,root,lis2):
        if root:
            lis2.append(str(root.val))
            if root.left == None and root.right == None:
                k = "".join(lis2)
                print(k)
                self.lis.append(int(k))
            else:
                self.check(root.left,lis2.copy())
                self.check(root.right,lis2.copy())
        
            
            
    def sumNumbers(self, root: TreeNode) -> int:
        self.lis = []
        lis2=[]
        self.check(root,lis2)
        return sum(self.lis)
