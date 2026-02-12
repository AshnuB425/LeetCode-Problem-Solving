class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        c=0
        s=nums[-1]
        for i in range(len(nums)-2,-1,-1):
            if nums[i]>(s/(len(nums)-i-1)):
                c+=1
            s+=nums[i]
        return c
