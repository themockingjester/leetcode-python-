"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def check(self,root,level):
        if root:
            if level not in self.dic:
                self.dic[level]=[root]
            else:
                self.dic[level].append(root)
            self.check(root.left,level+1)
            self.check(root.right,level+1)
    def connect(self, root: 'Node') -> 'Node':
        self.dic = {}
        self.check(root,0)
        for i in self.dic:
            k = self.dic[i]
            for j in range(len(k)-1):
                
                k[j].next = k[j+1]
        return root
                
        
