class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        table = [0] * (len(cost) + 1)

        for i in range(2, len(table)):
            table[i] = min(table[i - 1] + cost[i - 1], table[i - 2] + cost[i - 2])
        
        return table[-1]