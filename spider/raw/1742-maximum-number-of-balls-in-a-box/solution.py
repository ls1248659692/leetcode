class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        value = [0] * 46
        for i in range(lowLimit, highLimit+1):
            num = 0
            for j in str(i):
                num += int(j)
            value[num] += 1
        return max(value)
