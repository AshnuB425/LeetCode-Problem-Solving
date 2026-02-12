class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        a=sum(cost)
        d=[0]*26
        for i in range(len(s)):
            d[ord(s[i])-97]+=cost[i]
        maxi=0
        for i in d:
            maxi=max(maxi,i)
        return a-maxi
