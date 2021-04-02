# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self,root,level):

        if root:
            if level not in self.dic:
                self.dic[level]=[root.val]
            else:
                self.dic[level].append(root.val)
            self.check(root.left,level+1)
            self.check(root.right,level+1)
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        self.dic = {}
        self.check(root,0)
        lis=[]
        
        for i in self.dic:
            if i%2==0:
                lis.append(self.dic[i])
            else:
                k = self.dic[i]
                lis.append(k[::-1])
            
        return lis
