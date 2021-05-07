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
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        self.dic={}
        self.check(root,0)
        lis = []
        for i in self.dic:
            l = len(self.dic[i])
            s = sum(self.dic[i])
            lis.append(s/l)
        return lis
