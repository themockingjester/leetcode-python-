
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildtree(self,lis,node,isleft):
        maxi = max(lis)
        maxindex = lis.index(maxi)
        left = lis[0:maxindex]
        right = lis[maxindex+1:]
        if isleft==True:
            k = TreeNode(maxi)
            node.left = k
            if len(left)!=0:
            
                self.buildtree(left,node.left,True)
            if len(right)!=0:
                self.buildtree(right,node.left,False)
                
            
            
        else:
            
            k = TreeNode(maxi)
            node.right = k
            if len(left)!=0:
            
                self.buildtree(left,node.right,True)
            if len(right)!=0:
                self.buildtree(right,node.right,False)
            
        
        
        
            
            
        
        
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        maxi = max(nums)
        maxindex = nums.index(maxi)
        left = nums[0:maxindex]
        right = nums[maxindex+1:]
        node = TreeNode(maxi)
        if len(left)!=0:
            
            self.buildtree(left,node,True)
        if len(right)!=0:
            
            self.buildtree(right,node,False)
        return node
        
