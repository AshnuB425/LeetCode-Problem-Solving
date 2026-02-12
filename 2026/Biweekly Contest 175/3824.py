#Approach 1: Binary Search on Answer
class Solution:
    def minimumK(self, nums: List[int]) -> int:
        i,j=1,100005
        while i<=j:
            m=(i+j)//2
            ans=0
            for k in range(len(nums)):
                ans+=((nums[k]-1)//m)+1
            if ans<=(m*m):
                j=m-1
            else:
                i=m+1
        return i
