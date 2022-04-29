class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        factorsum = 0
        for j in range(1, int(num ** 0.5) + 1):
            if num % j == 0:
                factorsum = factorsum + j
                factorsum += num // j
        return factorsum == num * 2
