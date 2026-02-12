#Approach 1: Brute Force
class Solution:
    def countMonobit(self, n: int) -> int:
        c=0
        for i in range(n+1):
            if i&(i+1)==0:
                c+=1
        return c

#Approach 2: Bit Manipulation
class Solution:
    def countMonobit(self, n: int) -> int:
        return (n+1).bit_length()
