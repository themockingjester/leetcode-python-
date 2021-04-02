"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def check(self,root,level):

        if root:
            if level not in self.dic:
                self.dic[level]=[root.val]
            else:
                self.dic[level].append(root.val)
            for i in root.children:
                self.check(i,level+1)
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        self.dic = {}
        self.check(root,0)
        lis=[]
        for i in self.dic:
            
            lis.append(self.dic[i])
        return lis
