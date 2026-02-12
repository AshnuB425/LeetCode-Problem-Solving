#Approach 1: String Manipulation
class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        sc=0
        v,c=0,0
        for i in s:
            if i in 'aeiou':
                v+=1
            elif not i.isspace() and not i.isdigit():
                c+=1
        if c==0:
            return 0
        return v//c
