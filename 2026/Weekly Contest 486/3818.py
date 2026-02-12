#Approach 1: Simulation
class Solution:
    def minimumPrefixLength(self, nums: List[int]) -> int:
        mini=len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if nums[i+1]>nums[i]:
                mini=min(mini,i)
            else:
                break
        return mini
