# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        dic = {}
        level = 0
        
        if root==None:
            return False
        self.check(root,dic,x,y,level+1)
        #self.check(root.right,dic,x,y,level+1)
        if len(dic)!=2:
            return False
        else:
            if dic[x][0]!=dic[y][0]:
                if dic[x][1]==dic[y][1]:
                    return True
                else:
                    return False
            else:
                return False
        print(dic)
    def check(self,root,dic,x,y,level):
        if root==None:
            return False
        if root.left != None:
            if root.left.val == x:
                dic[x]=[root,level]
            if root.left.val == y:
                dic[y]=[root,level]
            self.check(root.left,dic,x,y,level+1)
        if root.right != None:
            if root.right.val == x:
                dic[x]=[root,level]
            if root.right.val==y:
                dic[y]=[root,level]
            self.check(root.right,dic,x,y,level+1)
        
        return False
        
