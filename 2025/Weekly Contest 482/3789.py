class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        if need1>need2:
            return min(cost1*need1+cost2*need2,costBoth*max(need1,need2),(cost1*(need1-need2))+need2*costBoth)
        elif need1<need2:
            return min(cost1*need1+cost2*need2,costBoth*max(need1,need2),(cost2*(need2-need1))+need1*costBoth)
        else:
            return min(cost1*need1+cost2*need2,costBoth*max(need1,need2))
