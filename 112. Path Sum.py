# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self,root,lis):
        if root  and self.output==False:
            if root.left == None and root.right == None:
                lis.append(root.val)
                if sum(lis)==self.target:
                    self.output = True
                    return
            else:
                lis.append(root.val)
                self.check(root.left,lis.copy())
                self.check(root.right,lis.copy())
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        lis = []
        self.output = False
        self.target = targetSum
        self.check(root,lis)
        return self.output
