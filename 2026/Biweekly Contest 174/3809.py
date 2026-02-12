#Approach 1: Math+Greedy
class Solution:
    def bestTower(self, towers: List[List[int]], center: List[int], radius: int) -> List[int]:
        c=[1e9,1e9]
        maxi=0
        for i in range(len(towers)):
            dis=abs(towers[i][0]-center[0])+abs(towers[i][1]-center[1])
            if dis<=radius:
                maxi=max(maxi,towers[i][2])
        for i in range(len(towers)):
            dis=abs(towers[i][0]-center[0])+abs(towers[i][1]-center[1])
            if dis<=radius:
                if towers[i][2]==maxi:
                    c=min(c,[towers[i][0],towers[i][1]])
        return [-1,-1] if c==[1e9,1e9] else c
