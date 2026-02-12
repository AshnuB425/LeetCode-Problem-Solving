#Approach 1: String Slicing
class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        return s[:k][::-1]+s[k:]

#Approach 2: 2 Pointers
class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        i,j=0,k-1
        s=list(s)
        while i<j:
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
        return "".join(s)
