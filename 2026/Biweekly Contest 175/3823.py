#Approach 1: Two Pointers
class Solution:
    def reverseByType(self, s: str) -> str:
        spe=[]
        nons=[]
        s=list(s)
        for i in s:
            if i.isalpha():
                spe.append(i)
            else:
                nons.append(i)
        a,b=len(spe)-1,len(nons)-1
        for i in range(len(s)):
            if s[i].isalpha():
                s[i]=spe[a]
                a-=1
            else:
                s[i]=nons[b]
                b-=1
        return "".join(s)
