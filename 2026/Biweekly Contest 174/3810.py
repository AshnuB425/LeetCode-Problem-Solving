#Approach 1: Set+Greedy
class Solution:
    def minOperations(self, nums: List[int], target: List[int]) -> int:
        s=set()
        for i in range(len(nums)):
            if nums[i]!=target[i]:
                if nums[i] not in s:
                    s.add(nums[i])
        return len(s)
