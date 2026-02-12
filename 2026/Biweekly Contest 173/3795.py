#Approach 1: Sliding Window
class Solution:
    def minLength(self, nums: List[int], k: int) -> int:
        mini=1e9
        d=[0]*(max(nums)+1)
        j=0
        s=0
        for i in range(len(nums)):
            d[nums[i]]+=1
            if d[nums[i]]==1:
                s+=nums[i]
            while s>=k:
                mini=min(mini,i-j+1)
                d[nums[j]]-=1
                if d[nums[j]]==0:
                    s-=nums[j]
                j+=1
        return -1 if mini==1e9 else mini
