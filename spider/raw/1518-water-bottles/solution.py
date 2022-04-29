class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        get = 0
        x = numBottles
        while x >= numExchange:
            get = x//numExchange
            reminder = x%numExchange
            numBottles = get + numBottles
            x = get + reminder
        return numBottles