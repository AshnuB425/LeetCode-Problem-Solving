#Approach 1: Set+Simulation
class Solution:
    def residuePrefixes(self, s: str) -> int:
        a=set()
        c=0
        for i in range(len(s)):
            a.add(s[i])
            if len(a)==(i+1)%3:
                c+=1
        return c
