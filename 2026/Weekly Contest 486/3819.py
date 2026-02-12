class Solution:
    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        neg=[]
        for i in nums:
            if i>=0:
                neg.append(i)
        p=0
        for i in range(len(nums)):
            if nums[i]>=0:
                nums[i]=(neg[(p+k)%len(neg)])
                p+=1
        return nums
