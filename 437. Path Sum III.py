# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self,root,lis):
        if root:
            lis.append(root.val)
            if sum(lis)==self.targetsum:
                self.total+=1
                
            
            self.check(root.left,lis.copy())
            self.check(root.right,lis)
    def traverse(self,root):
        if root:
            lis = []
            self.check(root,lis)
            self.traverse(root.left)
            self.traverse(root.right)
            
            
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        self.total = 0
        self.targetsum = targetSum
        
        self.traverse(root)
        return self.total
