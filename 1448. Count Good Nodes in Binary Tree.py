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
            
            if len(lis)!=0:
                if max(lis)==root.val:
                    print(lis)
                    self.ctr+=1
            else:
                self.ctr+=1
            
            self.check(root.left,lis.copy())
            self.check(root.right,lis)
    def goodNodes(self, root: TreeNode) -> int:
        self.ctr = 0
        self.check(root,[])
        return self.ctr
