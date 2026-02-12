class Solution:
    def largestEven(self, s: str) -> str:
        s=list(s)
        while len(s)>=1 and s[-1]=='1':
            s.pop()
        return "".join(s)
