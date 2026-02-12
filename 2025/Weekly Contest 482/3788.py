#Approach 1: Prefix Sum+ Suffix Minimum
class Solution:
    def maximumScore(self, nums: List[int]) -> int:
        pre=[]
        su=0
        for i in nums:
            su+=i
            pre.append(su)
        sf=[0]*len(nums)
        mini=3e15
        for i in range(len(nums)-1,-1,-1):
            mini=min(mini,nums[i])
            sf[i]=mini
        maxi=-3e15
        for i in range(len(nums)-1):
            maxi=max(maxi,pre[i]-sf[i+1])
        return maxi
