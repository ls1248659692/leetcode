class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        n = len(calories)
        window_sum = sum(calories[ :k]) 
        res = 0
        if window_sum < lower:
            res -= 1
        elif window_sum > upper:
            res += 1
        for R in range(k, n):      
            window_sum -= calories[R-k] 
            window_sum += calories[R]   
            if window_sum < lower:
                res -= 1
            elif window_sum > upper:
                res += 1
        return res
