class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        d= int(dividend/divisor) 
        return (2**31-1) if d>2**31-1 else d