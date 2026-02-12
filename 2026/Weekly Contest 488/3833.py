#Approach 1: Brute Force
class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        c=0
        for i in range(len(nums)):
            s=0
            for j in range(i+1,len(nums)):
                s+=nums[j]
            if len(nums)-i-1>0 and nums[i]>(s/(len(nums)-i-1)):
                c+=1
        return c

#Approach 2: Suffix Average
class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        c=0
        s=nums[-1]
        for i in range(len(nums)-2,-1,-1):
            if nums[i]>(s/(len(nums)-i-1)):
                c+=1
            s+=nums[i]
        return c
