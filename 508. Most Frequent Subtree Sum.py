# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverseindividually(self,root):
        if root:
            self.sum+=root.val
            self.traverseindividually(root.left)
            self.traverseindividually(root.right)
    def check(self,root):
        if root:
            self.sum = 0
            self.traverseindividually(root)
            self.lis.append(self.sum)
            self.check(root.left)
            self.check(root.right)
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        self.lis = []
        self.check(root)
        
        self.lis = sorted(self.lis)
        
        for i in range(len(self.lis)-1):
            if self.lis[i]!=self.lis[i+1]:
                pass
            else:
                break
        else:
            return self.lis
        
        k = list(set(self.lis))
        maxfreq = self.lis.count(k[0])
        for i in k:
            if self.lis.count(i)>maxfreq:
                maxfreq=self.lis.count(i)
        new = []
        
        for i in k:
            if self.lis.count(i)==maxfreq:
                new.append(i)
        return new
