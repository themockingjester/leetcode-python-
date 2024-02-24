# with stack
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        myStack = []
        ngeArr=[]
        for i in range(len(nums2)-1,-1,-1):
            curr = nums2[i]
            currAns = -1
            while len(myStack)>0:
                if myStack[-1]<=curr:
                    myStack.pop()
                else:
                    currAns = myStack[-1]
                    myStack.append(curr)
                    break
            else:
                myStack.append(curr)
            ngeArr.append(currAns)
        ngeArr=ngeArr[::-1]
        result=[]
        for i in nums1:
            result.append(ngeArr[nums2.index(i)])
        return result
            


        

# Another
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lis = []
        for i in range(len(nums1)):
            for j in range(nums2.index(nums1[i])+1,len(nums2)):
                if nums2[j]>nums1[i]:
                    lis.append(nums2[j])
                    break
            else:
                lis.append(-1)
        return lis
