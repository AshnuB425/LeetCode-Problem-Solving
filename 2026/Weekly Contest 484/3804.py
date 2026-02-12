#Approach 1: Brute Force+ Set
class Solution:
    def centeredSubarrays(self, nums: List[int]) -> int:
        c=0
        for i in range(len(nums)):
            a=set()
            s=0
            for j in range(i,len(nums)):
                a.add(nums[j])
                s+=nums[j]
                if s in a:
                    c+=1
        return c
