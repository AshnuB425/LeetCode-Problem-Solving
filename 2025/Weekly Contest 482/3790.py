#Approach 1: Math+Greedy
class Solution:
    def minAllOneMultiple(self, k: int) -> int:
        rem=0
        for i in range(k):
            rem=(rem*10+1)%k
            if rem==0:
                return i+1
        return -1
