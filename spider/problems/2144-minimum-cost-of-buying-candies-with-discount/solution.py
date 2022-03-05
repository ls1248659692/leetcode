class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        c= sorted(cost,reverse=True)
        return sum([c[i] for i in range(len(c)) if i%3<2])