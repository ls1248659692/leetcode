class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return num in [i**2 for i in range(1,5*10**4)]